<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0"
                xmlns:atom="http://www.w3.org/2005/Atom"
                xmlns="http://www.w3.org/2005/Atom">

  <!-- Drop empty title elements -->
  <xsl:template match="atom:title[not(node())]">
    <title>
      <xsl:apply-templates select="../atom:content/@*"/>
      <xsl:value-of select="../atom:content"/>
    </title>
  </xsl:template>

  <!-- Append title element if it's missing (instead of empty) -->
  <xsl:template match="atom:entry[not(atom:title)]">
    <xsl:copy>
      <xsl:apply-templates select="@*|node()"/>
      <title>
        <xsl:value-of select="atom:content"/>
      </title>
    </xsl:copy>
  </xsl:template>

  <!-- pass through everything else -->
  <xsl:template match="@*|node()">
    <xsl:copy>
      <xsl:apply-templates select="@*|node()"/>
    </xsl:copy>
  </xsl:template>

</xsl:stylesheet>
