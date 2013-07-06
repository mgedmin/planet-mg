<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0"
                xmlns:xhtml="http://www.w3.org/1999/xhtml"
                xmlns="http://www.w3.org/1999/xhtml">

  <!-- Modify links and add/replace target="_blank" -->
  <xsl:template match="xhtml:a">
    <xsl:copy>
      <xsl:attribute name="target">_blank</xsl:attribute>
      <xsl:apply-templates select="@*[name(.)!='target']|node()"/>
    </xsl:copy>
  </xsl:template>

  <!-- pass through everything else -->
  <xsl:template match="@*|node()">
    <xsl:copy>
      <xsl:apply-templates select="@*|node()"/>
    </xsl:copy>
  </xsl:template>

</xsl:stylesheet>

