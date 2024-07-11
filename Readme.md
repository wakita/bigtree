---
date: '2024-06-06'
category: 'research'
---

田中さんが研究対象としている巨大な木構造のデータとして、生物のカタログについて調査した。

# ColDP Archive との出会い

Wikipedia のページ群（[Primate](https://en.wikipedia.org/wiki/Primate), [Animal](https://en.wikipedia.org/wiki/Animal), [Kingdom (biology)](https://en.wikipedia.org/wiki/Kingdom_(biology)), [Domain (biology)](https://en.wikipedia.org/wiki/Domain_(biology)), [Pylogenetic tree](https://en.wikipedia.org/wiki/Phylogenetic_tree)-  (系統樹), [分類学](https://ja.wikipedia.org/wiki/%E5%88%86%E9%A1%9E%E5%AD%A6)）を巡るうちに [Encyclopedia of Life](https://ja.wikipedia.org/wiki/Encyclopedia_of_Life) の存在を学び、Encyclopedia of Life を訪れたところ、[Top](https://eol.org/), [Data Services](https://eol.org/docs/what-is-eol/data-services), [EOL Dynamic Hierarchy](https://eol.org/docs/eol-dynamic-hierarchy) と辿って以下の内容を含むデータが [ColDP Archive](https://api.checklistbank.org/dataset/296511/export.zip?extended=true&format=ColDP) (`1cbc4d4d-290a-4cc7-89ae-15cce5213bb5.zip`, 533MB) に含まれているらしいことを学んだ。

- **Viruses**: 8,345 taxa
- **Bacteria & Archaea**: 31,652 taxa
- **Protists**: 91,364 taxa
- **Fungi**: 148,073 taxa
- **Plants**: 459,180 taxa
- **Animals**: 1,666,175 taxa

# ColDP Archive (`1cbc4d4d-290a-4cc7-89ae-15cce5213bb5.zip`) の内容

- `metadata.yaml`
	- 56,831 行の YAML ファイル
	- 既知の種の約80%を包含していると思われる。230万種の現存種
	- 貢献者のリスト
- **TSV**
	- **Distribution.tsv** (2,663,779), Media.tsv,
	- **NameRelation.tsv** (859,279),
	- **NameUsage.tsv** (5,184,206),
	- **Reference.tsv** (1,631,265),
	- *SpeciesEstimate.tsv* (1,259), SpeciesInteraction.tsv, TaxonConceptRelation.tsv, TaxonProperty.tsv, TypeMaterial.tsv,
	- **VernacularName.tsv** (463,796): （土地に）固有な名称。jpn で検索すると和名が見られる。
- `source/*.yaml`
	- 743 - 1,708 行の YAML ファイル
- `logo.png`
- `reference.json`: 参考文献らしい

---
```
grep -i "homo sapiens" *.tsv
```

の結果：
```
NameUsage.tsv:5HYYJ 2144 6MB3T synonym Homo sapiens grimaldiensis Gregory, 1921 subspecies Homo sapiens grimaldiensis Gregory 1921 zoological https://www.itis.gov/servlet/SingleRpt/SingleRpt?search_topic=TSN&search_value=945629

NameUsage.tsv:5HYYG 2144 6MB3T synonym Homo sapiens cro-magnonensis Gregory, 1921 subspecies Homo sapiens cro-magnonensis Gregory 1921 zoological https://www.itis.gov/servlet/SingleRpt/SingleRpt?search_topic=TSN&search_value=945628

NameUsage.tsv:6MB3T 2144 636X2 accepted Homo sapiens Linnaeus, 1758 species Homo sapiens Linnaeus 1758 zoological acceptable b82cb41f-1572-4673-8c2e-f0f29b7ac6e8,a867b044-90c9-4271-92d1-1c64af7e61b1,45d1e2ff-8e23-4580-a506-38281657ddd5,c90648f7-dc88-4c38-8b84-a59feed80714 Colin P. Groves,Alfred L. Gardner,Anthony B. Rylands 2021-03-29 false https://www.itis.gov/servlet/SingleRpt/SingleRpt?search_topic=TSN&search_value=180092

NameUsage.tsv:5HYYH 2144 6MB3T synonym Homo sapiens cromagnonensis Gregory, 1921 subspecies Homo sapiens cromagnonensis Gregory 1921 zoological https://www.itis.gov/servlet/SingleRpt/SingleRpt?search_topic=TSN&search_value=945730

Reference.tsv:117938b9-9623-4e9f-91e4-658a6aec528b 2144 Morgan-Ryan, U.M., A. Fall, L. A. Ward, N. Hijjawi, I. Sulaiman, R. Fayer, R. C. Thompson, M. Olson,. (2002). Cryptosporidium hominis n. sp. (Apicomplexa: Cryptosporidiidae) from Homo sapiens. Journal of Eukaryotic Microbiology, Vol. 49. Morgan-Ryan, U.M., A. Fall, L. A. Ward, N. Hijjawi, I. Sulaiman, R. Fayer, R. C. Thompson, M. Olson, Cryptosporidium hominis n. sp. (Apicomplexa: Cryptosporidiidae) from Homo sapiens Journal of Eukaryotic Microbiology, vol. 49 2002
```

NameUsage.tsv:
- 6MB3T, 6MB3T, 6x6X2, 6MB3T
- Homo sapiens (grimaldiensis, cro-magnonensis, Linnaeus, cromagnonensis)
- `col:ID`: 項目の ID
- `col:parentID`: 親の項目の ID を指す
- `col:status`: accepted, synomym, ...
- `col:scientificName`
- `col:rank`: genus, family, species, class, order, ...
- `col:genericName`