# GPSP
This is the code for *GPSP: Graph Partition and Space Projection based approach for Heterogeneous Network Embedding*. The data and embeddings are aviable at https://drive.google.com/open?id=1PFp1E0O4I2LbitPo4_SV_0VP5hs2Z5gp.


<table>
<caption>Multi-label classification results for author embeddings in LINE-related algorithms</caption>
<thead>
<tr class="header">
<th style="text-align: center;">Metric</th>
<th style="text-align: center;">Method</th>
<th style="text-align: center;">10%</th>
<th style="text-align: center;">20%</th>
<th style="text-align: center;">30%</th>
<th style="text-align: center;">40%</th>
<th style="text-align: center;">50%</th>
<th style="text-align: center;">60%</th>
<th style="text-align: center;">70%</th>
<th style="text-align: center;">80%</th>
<th style="text-align: center;">90%</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td style="text-align: center;"></td>
<td style="text-align: center;">LINE-1st</td>
<td style="text-align: center;">0.7003</td>
<td style="text-align: center;">0.7069</td>
<td style="text-align: center;">0.7081</td>
<td style="text-align: center;">0.7087</td>
<td style="text-align: center;">0.7087</td>
<td style="text-align: center;">0.7084</td>
<td style="text-align: center;">0.7079</td>
<td style="text-align: center;">0.7087</td>
<td style="text-align: center;">0.7079</td>
</tr>
<tr class="even">
<td style="text-align: center;"></td>
<td style="text-align: center;">LINE-2nd</td>
<td style="text-align: center;">0.6436</td>
<td style="text-align: center;">0.6446</td>
<td style="text-align: center;">0.6457</td>
<td style="text-align: center;">0.6462</td>
<td style="text-align: center;">0.6463</td>
<td style="text-align: center;">0.6458</td>
<td style="text-align: center;">0.6456</td>
<td style="text-align: center;">0.6450</td>
<td style="text-align: center;">0.6470</td>
</tr>
<tr class="odd">
<td style="text-align: center;"></td>
<td style="text-align: center;">LINE-1st+2nd</td>
<td style="text-align: center;">0.7062</td>
<td style="text-align: center;">0.7064</td>
<td style="text-align: center;">0.7067</td>
<td style="text-align: center;">0.7075</td>
<td style="text-align: center;">0.7074</td>
<td style="text-align: center;">0.7077</td>
<td style="text-align: center;">0.7062</td>
<td style="text-align: center;">0.7072</td>
<td style="text-align: center;">0.7075</td>
</tr>
<tr class="even">
<td style="text-align: center;"></td>
<td style="text-align: center;">PTE</td>
<td style="text-align: center;">0.7122</td>
<td style="text-align: center;">0.7125</td>
<td style="text-align: center;">0.7129</td>
<td style="text-align: center;">0.7135</td>
<td style="text-align: center;">0.7133</td>
<td style="text-align: center;">0.7138</td>
<td style="text-align: center;">0.7140</td>
<td style="text-align: center;">0.7135</td>
<td style="text-align: center;">0.7138</td>
</tr>
<tr class="odd">
<td style="text-align: center;"></td>
<td style="text-align: center;">GPSPL-author 1st</td>
<td style="text-align: center;">0.6390</td>
<td style="text-align: center;">0.6420</td>
<td style="text-align: center;">0.6430</td>
<td style="text-align: center;">0.6436</td>
<td style="text-align: center;">0.6439</td>
<td style="text-align: center;">0.6432</td>
<td style="text-align: center;">0.6426</td>
<td style="text-align: center;">0.6448</td>
<td style="text-align: center;">0.6455</td>
</tr>
<tr class="even">
<td style="text-align: center;"></td>
<td style="text-align: center;">GPSPL-author 2nd</td>
<td style="text-align: center;">0.6162</td>
<td style="text-align: center;">0.6179</td>
<td style="text-align: center;">0.6184</td>
<td style="text-align: center;">0.6186</td>
<td style="text-align: center;">0.6181</td>
<td style="text-align: center;">0.6181</td>
<td style="text-align: center;">0.6183</td>
<td style="text-align: center;">0.6199</td>
<td style="text-align: center;">0.6212</td>
</tr>
<tr class="odd">
<td style="text-align: center;"></td>
<td style="text-align: center;">GPSPL-author 1st+2nd</td>
<td style="text-align: center;">0.6487</td>
<td style="text-align: center;">0.6509</td>
<td style="text-align: center;">0.6515</td>
<td style="text-align: center;">0.6519</td>
<td style="text-align: center;">0.6522</td>
<td style="text-align: center;">0.6515</td>
<td style="text-align: center;">0.6519</td>
<td style="text-align: center;">0.6534</td>
<td style="text-align: center;">0.6540</td>
</tr>
<tr class="even">
<td style="text-align: center;"></td>
<td style="text-align: center;">GPSPL-paper 1st</td>
<td style="text-align: center;">0.7118</td>
<td style="text-align: center;">0.7148</td>
<td style="text-align: center;">0.7136</td>
<td style="text-align: center;">0.7156</td>
<td style="text-align: center;">0.7167</td>
<td style="text-align: center;">0.7127</td>
<td style="text-align: center;">0.7219</td>
<td style="text-align: center;">0.7206</td>
<td style="text-align: center;">0.7227</td>
</tr>
<tr class="odd">
<td style="text-align: center;"></td>
<td style="text-align: center;">GPSPL-paper 2nd</td>
<td style="text-align: center;">0.6532</td>
<td style="text-align: center;">0.6546</td>
<td style="text-align: center;">0.6553</td>
<td style="text-align: center;">0.6554</td>
<td style="text-align: center;">0.6546</td>
<td style="text-align: center;">0.6540</td>
<td style="text-align: center;">0.6552</td>
<td style="text-align: center;">0.6521</td>
<td style="text-align: center;">0.6565</td>
</tr>
<tr class="even">
<td style="text-align: center;"></td>
<td style="text-align: center;">GPSPL-paper 1st+2nd</td>
<td style="text-align: center;">0.7235</td>
<td style="text-align: center;">0.7247</td>
<td style="text-align: center;">0.7247</td>
<td style="text-align: center;">0.7252</td>
<td style="text-align: center;">0.7256</td>
<td style="text-align: center;">0.7250</td>
<td style="text-align: center;">0.7262</td>
<td style="text-align: center;">0.7256</td>
<td style="text-align: center;">0.7267</td>
</tr>
<tr class="odd">
<td style="text-align: center;"></td>
<td style="text-align: center;">GPSPL 1st</td>
<td style="text-align: center;">0.7344</td>
<td style="text-align: center;">0.7378</td>
<td style="text-align: center;">0.7397</td>
<td style="text-align: center;">0.7396</td>
<td style="text-align: center;">0.7391</td>
<td style="text-align: center;">0.7401</td>
<td style="text-align: center;">0.7410</td>
<td style="text-align: center;">0.7425</td>
<td style="text-align: center;">0.7388</td>
</tr>
<tr class="even">
<td style="text-align: center;"></td>
<td style="text-align: center;">GPSPL 2nd</td>
<td style="text-align: center;">0.7121</td>
<td style="text-align: center;">0.7128</td>
<td style="text-align: center;">0.7141</td>
<td style="text-align: center;">0.7130</td>
<td style="text-align: center;">0.7148</td>
<td style="text-align: center;">0.7146</td>
<td style="text-align: center;">0.7137</td>
<td style="text-align: center;">0.7145</td>
<td style="text-align: center;">0.7159</td>
</tr>
<tr class="odd">
<td style="text-align: center;"></td>
<td style="text-align: center;">GPSPL 1st+2nd</td>
<td style="text-align: center;"><strong>0.7512</strong></td>
<td style="text-align: center;"><strong>0.7540</strong></td>
<td style="text-align: center;"><strong>0.7557</strong></td>
<td style="text-align: center;"><strong>0.7564</strong></td>
<td style="text-align: center;"><strong>0.7564</strong></td>
<td style="text-align: center;"><strong>0.7558</strong></td>
<td style="text-align: center;"><strong>0.7554</strong></td>
<td style="text-align: center;"><strong>0.7574</strong></td>
<td style="text-align: center;"><strong>0.7552</strong></td>
</tr>
<tr class="even">
<td style="text-align: center;"></td>
<td style="text-align: center;">LINE 1st</td>
<td style="text-align: center;">0.6996</td>
<td style="text-align: center;">0.7050</td>
<td style="text-align: center;">0.7061</td>
<td style="text-align: center;">0.7069</td>
<td style="text-align: center;">0.7067</td>
<td style="text-align: center;">0.7062</td>
<td style="text-align: center;">0.7056</td>
<td style="text-align: center;">0.7063</td>
<td style="text-align: center;">0.7059</td>
</tr>
<tr class="odd">
<td style="text-align: center;"></td>
<td style="text-align: center;">LINE 2nd</td>
<td style="text-align: center;">0.6389</td>
<td style="text-align: center;">0.6400</td>
<td style="text-align: center;">0.6413</td>
<td style="text-align: center;">0.6417</td>
<td style="text-align: center;">0.6419</td>
<td style="text-align: center;">0.6415</td>
<td style="text-align: center;">0.6409</td>
<td style="text-align: center;">0.6403</td>
<td style="text-align: center;">0.6426</td>
</tr>
<tr class="even">
<td style="text-align: center;"></td>
<td style="text-align: center;">LINE 1st+2nd</td>
<td style="text-align: center;">0.7032</td>
<td style="text-align: center;">0.7034</td>
<td style="text-align: center;">0.7036</td>
<td style="text-align: center;">0.7046</td>
<td style="text-align: center;">0.7043</td>
<td style="text-align: center;">0.7049</td>
<td style="text-align: center;">0.7035</td>
<td style="text-align: center;">0.7044</td>
<td style="text-align: center;">0.7036</td>
</tr>
<tr class="odd">
<td style="text-align: center;"></td>
<td style="text-align: center;">PTE</td>
<td style="text-align: center;">0.7089</td>
<td style="text-align: center;">0.7093</td>
<td style="text-align: center;">0.7094</td>
<td style="text-align: center;">0.7098</td>
<td style="text-align: center;">0.7101</td>
<td style="text-align: center;">0.7104</td>
<td style="text-align: center;">0.7090</td>
<td style="text-align: center;">0.7099</td>
<td style="text-align: center;">0.7094</td>
</tr>
<tr class="even">
<td style="text-align: center;"></td>
<td style="text-align: center;">GPSPL-author 1st</td>
<td style="text-align: center;">0.6399</td>
<td style="text-align: center;">0.6427</td>
<td style="text-align: center;">0.6434</td>
<td style="text-align: center;">0.6439</td>
<td style="text-align: center;">0.6438</td>
<td style="text-align: center;">0.6436</td>
<td style="text-align: center;">0.6424</td>
<td style="text-align: center;">0.6451</td>
<td style="text-align: center;">0.6451</td>
</tr>
<tr class="odd">
<td style="text-align: center;"></td>
<td style="text-align: center;">GPSPL-author 2nd</td>
<td style="text-align: center;">0.6119</td>
<td style="text-align: center;">0.6136</td>
<td style="text-align: center;">0.6141</td>
<td style="text-align: center;">0.6143</td>
<td style="text-align: center;">0.6140</td>
<td style="text-align: center;">0.6138</td>
<td style="text-align: center;">0.6138</td>
<td style="text-align: center;">0.6162</td>
<td style="text-align: center;">0.6169</td>
</tr>
<tr class="even">
<td style="text-align: center;"></td>
<td style="text-align: center;">GPSPL-author 1st+2nd</td>
<td style="text-align: center;">0.6477</td>
<td style="text-align: center;">0.6498</td>
<td style="text-align: center;">0.6506</td>
<td style="text-align: center;">0.6507</td>
<td style="text-align: center;">0.6508</td>
<td style="text-align: center;">0.6501</td>
<td style="text-align: center;">0.6506</td>
<td style="text-align: center;">0.6529</td>
<td style="text-align: center;">0.6528</td>
</tr>
<tr class="odd">
<td style="text-align: center;"></td>
<td style="text-align: center;">GPSPL-paper 1st</td>
<td style="text-align: center;">0.7087</td>
<td style="text-align: center;">0.7112</td>
<td style="text-align: center;">0.7099</td>
<td style="text-align: center;">0.7120</td>
<td style="text-align: center;">0.7130</td>
<td style="text-align: center;">0.7083</td>
<td style="text-align: center;">0.7198</td>
<td style="text-align: center;">0.7177</td>
<td style="text-align: center;">0.7211</td>
</tr>
<tr class="even">
<td style="text-align: center;"></td>
<td style="text-align: center;">GPSPL-paper 2nd</td>
<td style="text-align: center;">0.6557</td>
<td style="text-align: center;">0.6574</td>
<td style="text-align: center;">0.6580</td>
<td style="text-align: center;">0.6582</td>
<td style="text-align: center;">0.6571</td>
<td style="text-align: center;">0.6570</td>
<td style="text-align: center;">0.6578</td>
<td style="text-align: center;">0.6550</td>
<td style="text-align: center;">0.6591</td>
</tr>
<tr class="odd">
<td style="text-align: center;"></td>
<td style="text-align: center;">GPSPL-paper 1st+2nd</td>
<td style="text-align: center;">0.7212</td>
<td style="text-align: center;">0.7226</td>
<td style="text-align: center;">0.7226</td>
<td style="text-align: center;">0.7230</td>
<td style="text-align: center;">0.7231</td>
<td style="text-align: center;">0.7229</td>
<td style="text-align: center;">0.7243</td>
<td style="text-align: center;">0.7232</td>
<td style="text-align: center;">0.7251</td>
</tr>
<tr class="even">
<td style="text-align: center;"></td>
<td style="text-align: center;">GPSPL 1st</td>
<td style="text-align: center;">0.7318</td>
<td style="text-align: center;">0.7356</td>
<td style="text-align: center;">0.7369</td>
<td style="text-align: center;">0.7369</td>
<td style="text-align: center;">0.7361</td>
<td style="text-align: center;">0.7374</td>
<td style="text-align: center;">0.7388</td>
<td style="text-align: center;">0.7402</td>
<td style="text-align: center;">0.7364</td>
</tr>
<tr class="odd">
<td style="text-align: center;"></td>
<td style="text-align: center;">GPSPL 2nd</td>
<td style="text-align: center;">0.7111</td>
<td style="text-align: center;">0.7117</td>
<td style="text-align: center;">0.7132</td>
<td style="text-align: center;">0.7119</td>
<td style="text-align: center;">0.7139</td>
<td style="text-align: center;">0.7137</td>
<td style="text-align: center;">0.7130</td>
<td style="text-align: center;">0.7136</td>
<td style="text-align: center;">0.7155</td>
</tr>
<tr class="even">
<td style="text-align: center;"></td>
<td style="text-align: center;">GPSPL 1st+2nd</td>
<td style="text-align: center;"><strong>0.7482</strong></td>
<td style="text-align: center;"><strong>0.7513</strong></td>
<td style="text-align: center;"><strong>0.7527</strong></td>
<td style="text-align: center;"><strong>0.7534</strong></td>
<td style="text-align: center;"><strong>0.7534</strong></td>
<td style="text-align: center;"><strong>0.7529</strong></td>
<td style="text-align: center;"><strong>0.7526</strong></td>
<td style="text-align: center;"><strong>0.7544</strong></td>
<td style="text-align: center;"><strong>0.7522</strong></td>
</tr>
</tbody>
</table>

: Multi-label classification results for author embeddings in
LINE-related algorithms



## Requirement
* Python 3.5
* Pandas
* NLTK
* Scikit-Learn


\RestyleAlgo{boxruled}
\KwData{The heterogeneous information network $G=(V,E,T)$, number of negative samples $n$, number of walks per node $w$, walk length $l$, embedding dimension $d$, neighborhood size $k$.}
\KwResult{The latent vertex embeddings $X\in R^{|V|\times d}$}
subnetworkList = EdgeTypedBasedGraphPartition($G$)
homogeneousEmbeddingList projectiveEmbeddingList  $X$
