body,html {
    background-color: #161616;
    font-family: Inter,Hiragino Kaku Gothic ProN,Hiragino Sans,Meiryo,sans-serif;
    -webkit-font-smoothing: antialiased;
    letter-spacing: .01em!important;
    min-width: 100%!important;
    scroll-behavior: smooth;
    scroll-padding-top: 72px;
    margin: 0;
    padding: 0
}

.true {
    overflow-y: hidden
}

a {
    display: block;
    text-decoration: none;
    color: #161616
}

a,button {
    cursor: pointer
}

ol,ul {
    list-style: none;
    padding: 0
}

blockquote,body,dd,dl,figure,h1,h2,h3,h4,ol,p,ul {
    margin: 0
}

input,select,textarea {
    -webkit-appearance: none;
    -moz-appearance: none;
    appearance: none
}

input:focus {
    outline: none;
    background: none
}

input[type=checkbox],input[type=radio] {
    position: absolute;
    opacity: 0;
    -moz-appearance: none;
    appearance: none;
    -webkit-appearance: none
}

input[type=checkbox]:focus:not(:fous-visible)+.checkbox-box {
    outline: none
}

input[type=checkbox]:focus-visible+.checkbox-box {
    outline: 1px solid #ec4899
}

select {
    border: none
}

select,textarea {
    -webkit-appearance: none;
    -moz-appearance: none;
    appearance: none;
    outline: none;
    background: transparent
}

textarea {
    resize: none;
    padding: 0;
    border: 0
}

.favorites .pageHeader {
    padding: 32px 16px
}

.favorites .pageHeader .inner .descriptionBox {
    display: flex;
    align-items: center;
    gap: 16px;
    width: 100%;
    max-width: 100%
}

.favorites .pageHeader .inner .descriptionBox:has(.dropdownButton) {
    width: -moz-max-content;
    width: max-content
}

.favorites .pageHeader .inner .descriptionBox .h1 {
    font-size: 28px;
    line-height: 32px;
    font-weight: 700;
    width: -moz-max-content;
    width: max-content;
    max-width: calc(100% - 48px);
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap
}

@media screen and (min-width: 1024px) {
    .favorites .pageHeader .inner .descriptionBox .h1 {
        font-size:32px;
        line-height: 40px
    }
}

.favorites .pageHeader .inner .descriptionBox .dropdownButton {
    display: flex;
    align-items: center;
    justify-content: center;
    background-color: hsla(0,0%,100%,.15);
    border: 1px solid hsla(0,0%,100%,.05);
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    border-radius: 50px;
    width: 32px;
    height: 32px;
    transition: all .2s
}

.favorites .pageHeader .inner .descriptionBox .dropdownButton:active {
    transform: scale(.96)
}

@media screen and (min-width: 1024px) {
    .favorites .pageHeader .inner .descriptionBox .dropdownButton:hover {
        background-color:hsla(0,0%,100%,.25);
        transition: all .2s
    }
}

.favorites .pageHeader .inner .p {
    font-size: 14px;
    line-height: 20px;
    color: #a0a0a0;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap
}

.favorites .pageHeader .inner .tabList {
    display: flex;
    background-color: #2e2e2e;
    width: -moz-max-content;
    width: max-content;
    padding: 4px;
    border-radius: 50px
}

.favorites .pageHeader .inner .tabList .listItem button {
    display: flex;
    justify-content: center;
    padding: 6px 12px;
    font-size: 14px;
    line-height: 20px;
    background-color: #2e2e2e;
    color: #d4d4d4;
    border-radius: 50px;
    transition: .2s
}

.favorites .pageHeader .inner .tabList .listItem button:hover {
    background-color: #3e3e3e
}

.favorites .pageHeader .inner .tabList .listItem .active {
    background-color: #161616;
    box-shadow: 0 2px 2px 0 rgba(0,0,0,.25);
    color: #fff
}

.favorites .pageHeader .inner .tabList .listItem .active:hover {
    background-color: #1c1c1c
}

.popupInner {
    margin: 0
}

.popupInner .popupTitle {
    font-size: 20px;
    line-height: 28px;
    font-weight: 700
}

.popupInner .textInputWrapper .textInput,.popupInner .textareaWrapper .textarea {
    background-color: #2e2e2e;
    border: 1px solid #3e3e3e
}

.popupInner .textareaWrapper .textarea {
    height: 96px
}

.popupInner .popupButtonsBox {
    display: flex;
    justify-content: flex-end;
    gap: 16px
}

.upgradeAlert {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 320px
}

.upgradeAlert .alertTitle {
    font-size: 24px;
    line-height: 32px;
    font-weight: 700;
    text-align: center
}

.upgradeAlert .alertDescription {
    text-align: center;
    font-size: 16px;
    line-height: 24px;
    color: #d4d4d4
}

.haveLocalSidebar {
    display: flex;
    width: 100%;
    margin-top: 56px
}

@media screen and (min-width: 1024px) {
    .haveLocalSidebar {
        width:calc(100% - 56px);
        margin-left: auto
    }
}

.haveLocalSidebar .layoutWrapper {
    width: 100%
}

.haveLocalSidebar .layoutWrapper .main {
    min-height: calc(100vh - 56px);
    padding-bottom: 64px
}

.haveLocalSidebar .layoutWrapper .main .pageTitleWrapper {
    padding: 32px 16px 16px
}

.haveLocalSidebar .layoutWrapper .main .pageTitleWrapper .pageTitle {
    font-size: 24px;
    line-height: 32px;
    font-weight: 700
}

@media screen and (min-width: 1024px) {
    .haveLocalSidebar .layoutWrapper {
        width:calc(100% - 272px);
        margin-left: auto
    }
}

.notHaveLocalSidebar {
    width: 100%;
    overflow: scroll;
    margin-top: 56px
}

@media screen and (min-width: 1024px) {
    .notHaveLocalSidebar {
        width:calc(100% - 56px);
        margin-left: auto
    }
}

.notHaveLocalSidebar .layoutWrapper {
    height: 100%
}

.notHaveLocalSidebar .layoutWrapper .main {
    min-height: calc(100vh - 56px);
    height: -moz-max-content;
    height: max-content
}

.notHaveLocalSidebar .layoutWrapper .main .pageTitleWrapper {
    padding: 32px 16px 16px
}

.notHaveLocalSidebar .layoutWrapper .main .pageTitleWrapper .pageTitle {
    font-size: 24px;
    line-height: 32px;
    font-weight: 700
}

.appHeader {
    display: flex;
    align-items: center;
    flex-direction: column-reverse;
    gap: 32px;
    padding: 64px 32px;
    background: linear-gradient(180deg,#000,transparent)
}

@media screen and (min-width: 640px) {
    .appHeader {
        flex-direction:row;
        justify-content: space-between;
        align-items: flex-start;
        padding: 64px
    }
}

.appHeader .appInfo {
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 100%
}

@media screen and (min-width: 640px) {
    .appHeader .appInfo {
        align-items:flex-start;
        width: calc(100% - 172px)
    }
}

.appHeader .appInfo .labelMd {
    width: -moz-max-content;
    width: max-content;
    padding: 4px 8px;
    outline: 1px solid #3e3e3e;
    outline-offset: -1px;
    border-radius: 6px;
    font-size: 14px;
    line-height: 20px;
    color: #d4d4d4;
    transition: .2s
}

@media screen and (min-width: 640px) {
    .appHeader .appInfo .labelMd:hover {
        background-color:#232323;
        transition: .2s
    }
}

.appHeader .appInfo .appTexts {
    width: 100%
}

.appHeader .appInfo .appTexts .appDescriptionBox {
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 100%
}

@media screen and (min-width: 640px) {
    .appHeader .appInfo .appTexts .appDescriptionBox {
        align-items:flex-start
    }
}

.appHeader .appInfo .appTexts .appDescriptionBox .appTitle {
    max-width: 100%;
    font-size: 32px;
    line-height: 40px;
    font-weight: 700;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap
}

.appHeader .appInfo .appTexts .appDescriptionBox .appDescription {
    max-width: 100%;
    font-size: 14px;
    line-height: 20px;
    color: #d4d4d4;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap
}

.appHeader .appInfo .appTexts .appDescriptionBox .copyright {
    max-width: 100%;
    font-size: 12px;
    line-height: 16px;
    color: #ec4899;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
    transition: .2s
}

@media screen and (min-width: 640px) {
    .appHeader .appInfo .appTexts .appDescriptionBox .copyright:hover {
        text-decoration:underline;
        transition: .2s
    }
}

.appHeader .appInfo .favoriteButtonWrapper {
    display: flex;
    gap: 16px
}

.appHeader .iconWrapper {
    width: 144px;
    height: 144px;
    border-radius: 22.5%;
    border: 1px solid #232323;
    overflow: hidden;
    box-shadow: 0 4px 24px 0 rgba(0,0,0,.5)
}

.appHeader .iconWrapper .icon {
    width: 100%;
    height: 100%
}

.searchTitleContainer {
    display: flex;
    align-items: center;
    gap: 16px
}

.searchTitleContainer .pewviewImage {
    width: 56px;
    height: 56px;
    border-radius: 12px;
    -o-object-fit: cover;
    object-fit: cover;
    overflow: hidden;
    border: 1px solid #2e2e2e
}

.pricingSection .h1 {
    font-size: 24px;
    line-height: 32px;
    font-weight: 700;
    text-align: center
}

@media screen and (min-width: 1024px) {
    .pricingSection .h1 {
        font-size:32px;
        line-height: 40px
    }
}

.pricingSection .segmented-control {
    position: relative;
    display: flex;
    background-color: #232323;
    padding: 2px;
    border: 1px solid #2e2e2e;
    width: 320px;
    height: 44px;
    margin: auto;
    border-radius: 8px;
    overflow: hidden;
    cursor: pointer
}

.pricingSection .segmented-control li {
    position: relative;
    color: #7e7e7e;
    font-size: 14px;
    line-height: 20px;
    display: flex;
    justify-content: center;
    align-items: center;
    width: 50%;
    padding: 2px;
    font-weight: 700;
    z-index: 2
}

.pricingSection .segmented-control li .label {
    padding: 2px 6px;
    border-radius: 4px;
    background: rgba(34,197,94,.2);
    color: #4ade80;
    font-size: 12px;
    line-height: 16px;
    font-weight: 700
}

.pricingSection .segmented-control .active-segment {
    transition: .2s ease;
    color: #fff
}

.pricingSection .segmented-control span {
    position: absolute;
    width: calc(50% - 2px);
    background-color: #2e2e2e;
    top: 2px;
    bottom: 2px;
    left: 2px;
    border: 1px solid #3e3e3e;
    border-radius: 6px;
    z-index: 1;
    box-shadow: 0 2px 4px rgba(0,0,0,.1);
    transition: left .2s ease
}

.pricingSection .segmented-control li:first-child.active-segment~span {
    left: 2px
}

.pricingSection .segmented-control li:nth-child(2).active-segment~span {
    left: 50%
}

.pricingSection .planList {
    display: grid;
    grid-template-columns: 1fr;
    gap: 32px;
    width: 100%
}

@media screen and (min-width: 1024px) {
    .pricingSection .planList {
        grid-template-columns:1fr 1fr 1fr;
        width: 992px
    }
}

.pricingSection .planList>.listItem {
    position: relative;
    padding: 32px;
    border-radius: 16px;
    display: flex;
    flex-direction: column
}

.pricingSection .planList>.listItem .currentPlanLabel {
    position: absolute;
    top: 0;
    right: 0;
    display: flex;
    align-items: center;
    justify-content: center;
    width: -moz-max-content;
    width: max-content;
    height: 28px;
    padding: 0 16px;
    border-radius: 0 0 0 16px;
    background-color: #2563eb;
    color: #fff;
    font-size: 14px;
    line-height: 20px;
    font-weight: 700
}

.pricingSection .planList>.listItem .planTitle {
    font-size: 20px;
    line-height: 28px;
    font-weight: 700
}

.pricingSection .planList>.listItem .priceNumber {
    position: relative;
    gap: 16px;
    font-size: 36px;
    line-height: 40px;
    font-weight: 700
}

.pricingSection .planList>.listItem .priceNumber>.small {
    font-size: 22px;
    line-height: 28px;
    font-weight: 400
}

.pricingSection .planList>.listItem .priceNumber>.xsmall {
    font-size: 16px;
    line-height: 24px;
    font-weight: 400
}

.pricingSection .planList>.listItem .priceNumber .note {
    position: absolute;
    bottom: -24px;
    left: -14px;
    display: inline-block;
    font-size: 14px;
    line-height: 20px;
    font-weight: 400;
    color: #a0a0a0
}

.pricingSection .planList>.listItem .priceNumber .note>.small {
    font-size: 12px;
    line-height: 16px;
    font-weight: 400
}

.pricingSection .planList>.listItem .buttonSubText {
    position: absolute;
    bottom: -24px;
    left: 50%;
    transform: translateX(-50%);
    -webkit-transform: translateX(-50%);
    width: -moz-max-content;
    width: max-content;
    font-size: 12px;
    line-height: 16px;
    color: #a0a0a0
}

.pricingSection .planList>.listItem .planContentsList {
    display: flex;
    flex-direction: column;
    gap: 16px
}

.pricingSection .planList>.listItem .planContentsList .listItem {
    display: flex;
    align-items: center;
    gap: 8px
}

.pricingSection .planList .borderNormal {
    position: relative;
    z-index: 2;
    overflow: hidden;
    border: 2px solid #2e2e2e
}

.pricingSection .planList .borderNormal:before {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 224px;
    background: linear-gradient(147deg,#121212,transparent 50%);
    z-index: -1
}

.pricingSection .planList .borderNormal .span {
    color: #d4d4d4
}

.pricingSection .planList .borderPink {
    position: relative;
    z-index: 2;
    overflow: hidden;
    border: 2px solid #ec4899
}

.pricingSection .planList .borderPink:before {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 224px;
    background: linear-gradient(147deg,#550a40,transparent 50%);
    z-index: -1
}

.pricingSection .planList .borderPink .span {
    color: #fff
}

.pricingSection .planList .borderWhite {
    position: relative;
    z-index: 2;
    overflow: hidden;
    border: 2px solid #fff
}

.pricingSection .planList .borderWhite:before {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 224px;
    background: linear-gradient(147deg,#363636,transparent 50%);
    z-index: -1
}

.pricingSection .planList .borderWhite .span {
    color: #fff
}

.faqSection .h2 {
    font-size: 20px;
    line-height: 28px;
    font-weight: 700;
    text-align: center
}

@media screen and (min-width: 1024px) {
    .faqSection .h2 {
        font-size:24px;
        line-height: 32px
    }
}

.faqSection .faq-wrapper {
    width: 100%;
    max-width: 680px
}

.faqSection .faq-wrapper details {
    padding: 8px 0;
    border-bottom: 1px solid #232323
}

.faqSection .faq-wrapper details[open] .icon {
    transform: rotate(180deg)
}

.faqSection .faq-wrapper summary {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 12px 0;
    cursor: pointer
}

.faqSection .faq-wrapper summary::-webkit-details-marker {
    display: none
}

.faqSection .faq-wrapper summary span {
    width: calc(100% - 36px);
    font-size: 16px;
    line-height: 24px
}

.faqSection .faq-wrapper summary .icon {
    font-size: 20px;
    line-height: 28px;
    transition: transform .2s;
    color: #7e7e7e
}

.faqSection .faq-wrapper .accordion-content {
    padding: 12px 0
}

.faqSection .faq-wrapper .accordion-content span {
    font-size: 16px;
    line-height: 24px;
    color: #a0a0a0
}

.faqSection .link {
    display: inline;
    text-decoration: underline
}

.faqSection .note {
    font-size: 14px;
    line-height: 20px;
    color: #a0a0a0
}

.dropdownButton .buttonText {
    font-weight: 700
}

.dropdownButton .proLabel {
    position: relative;
    font-size: 12px;
    line-height: 16px;
    font-weight: 700;
    padding: 2px 8px;
    border-radius: 50px;
    background-color: #fff;
    color: #161616
}

.dropdownButton .proLabel:before {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    border-radius: 50px;
    border: 2px solid transparent;
    background-image: linear-gradient(135deg,#f957dc,#b780ed 50%,#74a9ff);
    background-origin: border-box;
    background-clip: border-box;
    -webkit-mask-image: linear-gradient(#fff 0 0),linear-gradient(#fff 0 0);
    -webkit-mask-clip: padding-box,border-box;
    -webkit-mask-composite: destination-out;
    mask-image: linear-gradient(#fff 0 0),linear-gradient(#fff 0 0);
    mask-clip: padding-box,border-box;
    -webkit-mask-composite: xor;
    mask-composite: exclude
}

.form-section {
    width: 100%;
    padding: 64px 16px 0
}

@media screen and (min-width: 1024px) {
    .form-section {
        width:680px;
        margin: auto
    }
}

.form-section .inner .h1 {
    font-size: 24px;
    line-height: 32px;
    font-weight: 700
}

.form-section .inner .form {
    display: flex;
    flex-direction: column;
    gap: 32px
}

.form-section .inner .planCard {
    border-radius: 10px;
    border: 1px solid #2e2e2e;
    overflow: hidden
}

.form-section .inner .planCard .cardHeader {
    display: flex;
    align-items: center;
    gap: 16px;
    width: 100%;
    height: 40px;
    padding: 0 32px;
    background-color: #2e2e2e
}

.form-section .inner .planCard .cardHeader .cardTitle {
    font-size: 14px;
    line-height: 20px;
    font-weight: 700
}

.form-section .inner .planCard .cardHeader .label {
    color: #a78bfa;
    background-color: rgba(167,139,250,.231);
    border-radius: 4px
}

.form-section .inner .planCard .cardContent {
    padding: 32px;
    background-color: #232323
}

.form-section .inner .planCard .cardContent .titleSection {
    display: flex;
    align-items: center
}

.form-section .inner .planCard .cardContent .titleSection .planName {
    font-size: 24px;
    line-height: 32px;
    font-weight: 700
}

.form-section .inner .planCard .cardContent .titleSection .planName small {
    font-size: 14px;
    line-height: 20px;
    font-weight: 400
}

.form-section .inner .planCard .cardContent .titleSection .divider {
    width: 1px;
    height: 20px;
    background-color: #707070;
    margin: 0 16px
}

.form-section .inner .planCard .cardContent .titleSection .teamProfileWrapper {
    display: flex;
    align-items: center;
    gap: 8px
}

.form-section .inner .planCard .cardContent .titleSection .teamProfileWrapper .avatarWrapper {
    width: 32px;
    height: 32px;
    border-radius: 4px;
    overflow: hidden
}

.form-section .inner .planCard .cardContent .titleSection .teamProfileWrapper .avatarWrapper .avatar {
    width: 100%;
    height: 100%;
    -o-object-fit: cover;
    object-fit: cover
}

.form-section .inner .planCard .cardContent .titleSection .teamProfileWrapper .avatarWrapper .avatarFallback {
    width: 100%;
    height: 100%;
    background-color: #707070;
    color: #161616;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 700;
    font-size: 18px;
    line-height: 24px
}

.form-section .inner .planCard .cardContent .titleSection .teamProfileWrapper .teamName {
    font-size: 18px;
    line-height: 24px;
    font-weight: 700
}

.form-section .inner .planCard .cardContent .titleSection .teamProfileWrapper .label {
    width: -moz-max-content;
    width: max-content;
    border: 1px solid #3e3e3e;
    font-size: 12px;
    line-height: 16px
}

.form-section .inner .planCard .cardContent .description {
    font-size: 14px;
    line-height: 20px;
    color: #a0a0a0
}

.form-section .inner .planSection {
    border-top: 1px solid #2e2e2e
}

.doc-wrapper {
    padding: 0 16px
}

@media screen and (min-width: 1024px) {
    .doc-wrapper {
        width:768px;
        margin: auto;
        padding: 0
    }
}

.doc-wrapper h1 {
    margin: 32px 0;
    font-size: 28px;
    line-height: 32px;
    font-weight: 700
}

@media screen and (min-width: 1024px) {
    .doc-wrapper h1 {
        font-size:32px;
        line-height: 40px
    }
}

.doc-wrapper h2 {
    margin-top: 64px;
    font-size: 22px;
    line-height: 28px;
    font-weight: 700
}

@media screen and (min-width: 1024px) {
    .doc-wrapper h2 {
        font-size:24px;
        line-height: 32px
    }
}

.doc-wrapper h3 {
    margin-top: 32px;
    font-size: 18px;
    line-height: 24px;
    font-weight: 700
}

@media screen and (min-width: 1024px) {
    .doc-wrapper h3 {
        font-size:20px;
        line-height: 28px
    }
}

.doc-wrapper p {
    margin: 16px 0
}

.doc-wrapper ul {
    padding-left: 28px;
    margin: 16px 0
}

.doc-wrapper ul li {
    position: relative;
    margin-bottom: 8px
}

.doc-wrapper ul li:before {
    content: "";
    position: absolute;
    top: 10px;
    left: -18px;
    width: 6px;
    height: 6px;
    border-radius: 50px;
    background-color: #fff
}

.doc-wrapper ul li p {
    margin: 0
}

.doc-wrapper ul li ul li:before {
    content: "";
    position: absolute;
    top: 10px;
    left: -18px;
    width: 6px;
    height: 6px;
    border: 1px solid #fff;
    border-radius: 50px;
    background-color: transparent
}

.doc-wrapper ul li ul li ul li:before {
    content: "";
    position: absolute;
    top: 10px;
    left: -18px;
    width: 6px;
    height: 6px;
    border: 1px solid #fff;
    border-radius: 0;
    background-color: #fff
}

.doc-wrapper ol {
    padding-left: 28px;
    margin: 16px 0
}

.doc-wrapper ol li {
    position: relative;
    margin-bottom: 8px;
    list-style: decimal
}

.doc-wrapper ol li p {
    margin: 0
}

.doc-wrapper ol li ol li {
    list-style: lower-alpha
}

.doc-wrapper ol li ol li ol li {
    list-style: upper-roman
}

.doc-wrapper hr {
    border-color: #343434
}

.doc-wrapper a {
    display: inline;
    color: #3b82f6;
    text-decoration: underline
}

.doc-wrapper img {
    border: 1px solid #2e2e2e;
    border-radius: 8px;
    width: 100%;
    height: auto;
    margin: 16px 0;
    -o-object-fit: cover;
    object-fit: cover;
    overflow: hidden
}

@media screen and (min-width: 1024px) {
    .doc-wrapper img {
        border-radius:12px
    }
}

.notLoggedInWrwapper {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 32px;
    width: 100%;
    padding: 0 16px;
    margin-top: 64px
}

@media screen and (min-width: 1024px) {
    .notLoggedInWrwapper {
        width:680px;
        margin: 64px auto auto
    }
}

.notLoggedInWrwapper .iconBox {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 64px;
    height: 64px;
    border-radius: 50px;
    background-color: rgba(236,72,153,.145)
}

.notLoggedInWrwapper .h1 {
    font-size: 32px;
    line-height: 40px;
    font-weight: 700
}

.notLoggedInWrwapper .h2 {
    font-size: 24px;
    line-height: 32px;
    font-weight: 700;
    text-align: center
}

.notLoggedInWrwapper .description {
    font-size: 12px;
    line-height: 16px;
    color: #7e7e7e;
    text-align: center
}

.notLoggedInWrwapper .description .textLink {
    display: inline;
    text-decoration: underline
}

.articles-wrapper {
    padding: 0 16px
}

@media screen and (min-width: 1024px) {
    .articles-wrapper {
        width:768px;
        margin: auto;
        padding: 0
    }
}

.articles-wrapper .h1 {
    font-size: 28px;
    line-height: 32px;
    font-weight: 700
}

@media screen and (min-width: 1024px) {
    .articles-wrapper .h1 {
        font-size:32px;
        line-height: 40px
    }
}

.articles-wrapper .articles-list {
    position: relative
}

.articles-wrapper .articles-list:before {
    content: "";
    position: absolute;
    top: 8px;
    left: 6px;
    width: 2px;
    height: 100%;
    border: 2px solid #2e2e2e;
    border-radius: 50px
}

.articles-wrapper .articles-list .list-item {
    position: relative
}

.articles-wrapper .articles-list .list-item:before {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    width: 16px;
    height: 16px;
    background-color: #161616;
    border: 2px solid #fff;
    border-radius: 50px
}

@media screen and (min-width: 1024px) {
    .articles-wrapper .articles-list .list-item .list-item-inner:hover .h2 {
        text-decoration:underline
    }
}

.articles-wrapper .articles-list .list-item .list-item-inner .thumbnail-wrapper {
    width: 100%;
    aspect-ratio: 16/9;
    background-color: #232323;
    border: 1px solid #2e2e2e;
    border-radius: 8px
}

@media screen and (min-width: 1024px) {
    .articles-wrapper .articles-list .list-item .list-item-inner .thumbnail-wrapper {
        border-radius:12px
    }
}

.articles-wrapper .articles-list .list-item .list-item-inner .thumbnail-wrapper .thumbnail {
    width: 100%;
    height: 100%;
    -o-object-fit: cover;
    object-fit: cover;
    overflow: hidden
}

.articles-wrapper .articles-list .list-item .list-item-inner .label-box {
    display: flex;
    align-items: center;
    gap: 16px
}

.articles-wrapper .articles-list .list-item .list-item-inner .label-box .label-md {
    width: -moz-max-content;
    width: max-content;
    padding: 6px 12px;
    border: 1px solid #3e3e3e;
    border-radius: 6px;
    font-size: 14px;
    line-height: 20px;
    color: #fff
}

.articles-wrapper .articles-list .list-item .list-item-inner .label-box .date {
    font-size: 14px;
    line-height: 20px;
    color: #a0a0a0
}

.articles-wrapper .articles-list .list-item .list-item-inner .h2 {
    font-size: 22px;
    line-height: 28px;
    font-weight: 700
}

@media screen and (min-width: 1024px) {
    .articles-wrapper .articles-list .list-item .list-item-inner .h2 {
        font-size:24px;
        line-height: 32px
    }
}

.article-wrapper .article-title-section {
    background: linear-gradient(180deg,#050505,transparent);
    border-bottom: 1px solid #232323
}

.article-wrapper .article-title-section .inner {
    padding: 0 16px
}

@media screen and (min-width: 1024px) {
    .article-wrapper .article-title-section .inner {
        width:768px;
        margin: auto;
        padding: 0
    }
}

.article-wrapper .article-title-section .inner .back-button {
    display: flex;
    align-items: center;
    gap: 8px;
    padding: 6px 0
}

@media screen and (min-width: 1024px) {
    .article-wrapper .article-title-section .inner .back-button:hover .button-text {
        color:#a0a0a0;
        text-decoration: underline
    }
}

.article-wrapper .article-title-section .inner .back-button .button-text {
    font-size: 14px;
    line-height: 20px;
    color: #a0a0a0
}

.article-wrapper .article-title-section .inner .label-md {
    width: -moz-max-content;
    width: max-content;
    padding: 6px 12px;
    border: 1px solid #3e3e3e;
    border-radius: 6px;
    font-size: 14px;
    line-height: 20px;
    color: #fff
}

.article-wrapper .article-title-section .inner .h1 {
    font-size: 28px;
    line-height: 32px;
    font-weight: 700
}

@media screen and (min-width: 1024px) {
    .article-wrapper .article-title-section .inner .h1 {
        font-size:32px;
        line-height: 40px
    }
}

.article-wrapper .article-title-section .inner .author-info-wrapper {
    display: flex;
    align-items: center;
    justify-content: space-between
}

.article-wrapper .article-title-section .inner .author-info-wrapper .author-info-box {
    display: flex;
    align-items: center;
    gap: 8px
}

.article-wrapper .article-title-section .inner .author-info-wrapper .author-info-box .avatar {
    width: 40px;
    height: 40px;
    border: 1px solid #2e2e2e;
    border-radius: 50px
}

.article-wrapper .article-title-section .inner .author-info-wrapper .author-info-box .author-name {
    font-size: 14px;
    line-height: 20px;
    font-weight: 700
}

.article-wrapper .article-title-section .inner .author-info-wrapper .author-info-box .date {
    font-size: 12px;
    line-height: 16px;
    color: #a0a0a0
}

.article-wrapper .article-title-section .inner .author-info-wrapper .x-link {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 32px;
    height: 32px
}

.article-wrapper .article-title-section .inner .author-info-wrapper .x-link .icon {
    width: 16px;
    height: auto
}

.article-wrapper .article-content .inner {
    padding: 0 16px
}

@media screen and (min-width: 1024px) {
    .article-wrapper .article-content .inner {
        width:768px;
        margin: auto;
        padding: 0
    }
}

.article-wrapper .article-content .thumbnail-wrapper {
    width: 100%;
    aspect-ratio: 16/9;
    background-color: #232323;
    border: 1px solid #2e2e2e;
    border-radius: 8px
}

@media screen and (min-width: 1024px) {
    .article-wrapper .article-content .thumbnail-wrapper {
        border-radius:12px
    }
}

.article-wrapper .article-content .thumbnail-wrapper .thumbnail {
    width: 100%;
    height: 100%;
    -o-object-fit: cover;
    object-fit: cover;
    overflow: hidden
}

.article-wrapper .article-content h1 {
    margin: 32px 0;
    font-size: 28px;
    line-height: 32px;
    font-weight: 700
}

@media screen and (min-width: 1024px) {
    .article-wrapper .article-content h1 {
        font-size:32px;
        line-height: 40px
    }
}

.article-wrapper .article-content h2 {
    margin-top: 64px;
    font-size: 22px;
    line-height: 28px;
    font-weight: 700
}

@media screen and (min-width: 1024px) {
    .article-wrapper .article-content h2 {
        font-size:24px;
        line-height: 32px
    }
}

.article-wrapper .article-content h3 {
    margin-top: 32px;
    font-size: 18px;
    line-height: 24px;
    font-weight: 700
}

@media screen and (min-width: 1024px) {
    .article-wrapper .article-content h3 {
        font-size:20px;
        line-height: 28px
    }
}

.article-wrapper .article-content p {
    margin: 16px 0
}

.article-wrapper .article-content ul {
    padding-left: 28px;
    margin: 16px 0
}

.article-wrapper .article-content ul li {
    position: relative;
    margin-bottom: 8px
}

.article-wrapper .article-content ul li:before {
    content: "";
    position: absolute;
    top: 10px;
    left: -18px;
    width: 6px;
    height: 6px;
    border-radius: 50px;
    background-color: #fff
}

.article-wrapper .article-content ul li p {
    margin: 0
}

.article-wrapper .article-content ul li ul li:before {
    content: "";
    position: absolute;
    top: 10px;
    left: -18px;
    width: 6px;
    height: 6px;
    border: 1px solid #fff;
    border-radius: 50px;
    background-color: transparent
}

.article-wrapper .article-content ul li ul li ul li:before {
    content: "";
    position: absolute;
    top: 10px;
    left: -18px;
    width: 6px;
    height: 6px;
    border: 1px solid #fff;
    border-radius: 0;
    background-color: #fff
}

.article-wrapper .article-content ol {
    padding-left: 28px;
    margin: 16px 0
}

.article-wrapper .article-content ol li {
    position: relative;
    margin-bottom: 8px;
    list-style: decimal
}

.article-wrapper .article-content ol li p {
    margin: 0
}

.article-wrapper .article-content ol li ol li {
    list-style: lower-alpha
}

.article-wrapper .article-content ol li ol li ol li {
    list-style: upper-roman
}

.article-wrapper .article-content hr {
    border-color: #343434
}

.article-wrapper .article-content a {
    display: inline;
    color: #3b82f6;
    text-decoration: underline
}

.article-wrapper .article-content img {
    border: 1px solid #2e2e2e;
    border-radius: 8px;
    width: 100%;
    height: auto;
    margin: 16px 0;
    -o-object-fit: cover;
    object-fit: cover;
    overflow: hidden
}

@media screen and (min-width: 1024px) {
    .article-wrapper .article-content img {
        border-radius:12px
    }
}

.tiptap {
    max-width: 832px;
    padding: 32px;
    margin: auto;
    border: 1px solid #2e2e2e;
    border-radius: 10px
}

.tiptap h1 {
    margin: 32px 0;
    font-size: 32px;
    line-height: 40px;
    font-weight: 700
}

.tiptap h2 {
    margin-top: 64px;
    font-size: 24px;
    line-height: 32px;
    font-weight: 700
}

.tiptap h3 {
    margin-top: 32px;
    font-size: 20px;
    line-height: 28px;
    font-weight: 700
}

.tiptap p,.tiptap ul {
    margin: 16px 0
}

.tiptap ul {
    padding-left: 28px
}

.tiptap ul li {
    position: relative;
    margin-bottom: 8px
}

.tiptap ul li:before {
    content: "";
    position: absolute;
    top: 10px;
    left: -18px;
    width: 6px;
    height: 6px;
    border-radius: 50px;
    background-color: #fff
}

.tiptap ul li p {
    margin: 0
}

.tiptap ul li ul li:before {
    border: 1px solid #fff;
    border-radius: 50px;
    background-color: transparent
}

.tiptap ul li ul li ul li:before,.tiptap ul li ul li:before {
    content: "";
    position: absolute;
    top: 10px;
    left: -18px;
    width: 6px;
    height: 6px
}

.tiptap ul li ul li ul li:before {
    border: 1px solid #fff;
    border-radius: 0;
    background-color: #fff
}

.tiptap ol {
    padding-left: 28px;
    margin: 16px 0
}

.tiptap ol li {
    position: relative;
    margin-bottom: 8px;
    list-style: decimal
}

.tiptap ol li p {
    margin: 0
}

.tiptap ol li ol li {
    list-style: lower-alpha
}

.tiptap ol li ol li ol li {
    list-style: upper-roman
}

.tiptap hr {
    border-color: #343434
}

.tiptap a {
    display: inline;
    color: #3b82f6;
    text-decoration: underline
}

.tiptap img {
    margin: 16px 0;
    border: 1px solid #2e2e2e;
    border-radius: 8px
}

.textGray200 {
    color: #d4d4d4
}

.borderGray900 {
    border-color: #2e2e2e
}

.proButtonWrapper {
    padding: 2px;
    background: linear-gradient(138deg,#f957dc 37.44%,#72aeff 100.06%);
    border-radius: 50px;
    transition: .2s
}

.proButtonWrapper:active {
    transform: scale(.96)
}

.proButtonWrapperWithBadge {
    position: absolute;
    top: 0;
    right: -2px;
    border-radius: 50px;
    transition: .2s;
    z-index: 5;
    pointer-events: none
}

.textInputWrapper {
    display: flex;
    flex-direction: column;
    gap: 8px
}

.textInputWrapper .textInputLabel {
    display: flex;
    align-items: center;
    gap: 8px;
    font-size: 14px;
    line-height: 20px;
    color: #fff
}

.textInputWrapper .textInputLabel .requiredLabel {
    padding: 2px 6px;
    background-color: rgba(255,40,40,.25);
    border-radius: 4px;
    font-size: 12px;
    line-height: 16px;
    color: #ef4444
}

.textInputWrapper .textInputLabel .optionalLabel {
    padding: 2px 6px;
    background-color: #3e3e3e;
    border-radius: 4px;
    font-size: 12px;
    line-height: 16px;
    color: #d4d4d4
}

.textInputWrapper .textInput {
    align-items: center;
    justify-content: center;
    width: 100%;
    height: 40px;
    padding: 0 12px;
    background-color: #1c1c1c;
    border: 1px solid #2e2e2e;
    border-radius: 6px;
    transition: all .2s
}

.textInputWrapper .textInput::-moz-placeholder {
    color: #707070
}

.textInputWrapper .textInput::placeholder {
    color: #707070
}

.textInputWrapper .textInput:focus {
    border: 1px solid #707070;
    box-shadow: 0 0 0 4px hsla(0,0%,100%,.1);
    transition: all .2s
}

.textInputWrapper .textInput:disabled {
    color: #707070;
    cursor: not-allowed
}

.textInputWrapper .formErrorMessage {
    font-size: 12px;
    line-height: 16px;
    color: #ef4444
}

.textareaWrapper {
    display: flex;
    flex-direction: column;
    gap: 8px
}

.textareaWrapper .textareaLabel {
    display: flex;
    align-items: center;
    gap: 8px;
    font-size: 14px;
    line-height: 20px;
    color: #fff
}

.textareaWrapper .textareaLabel .requiredLabel {
    padding: 2px 6px;
    background-color: rgba(255,40,40,.25);
    border-radius: 4px;
    font-size: 12px;
    line-height: 16px;
    color: #ef4444
}

.textareaWrapper .textareaLabel .optionalLabel {
    padding: 2px 6px;
    background-color: #3e3e3e;
    border-radius: 4px;
    font-size: 12px;
    line-height: 16px;
    color: #d4d4d4
}

.textareaWrapper .textarea {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 100%;
    height: 160px;
    padding: 6px 12px;
    background-color: #1c1c1c;
    border: 1px solid #2e2e2e;
    border-radius: 6px;
    transition: all .2s
}

.textareaWrapper .textarea::-moz-placeholder {
    color: #707070
}

.textareaWrapper .textarea::placeholder {
    color: #707070
}

.textareaWrapper .textarea:focus {
    border: 1px solid #707070;
    box-shadow: 0 0 0 4px hsla(0,0%,100%,.1);
    transition: all .2s
}

.textareaWrapper .formErrorMessage {
    font-size: 12px;
    line-height: 16px;
    color: #ef4444
}

.buttonFile {
    display: block;
    width: -moz-max-content;
    width: max-content;
    padding-right: 16px;
    cursor: pointer
}

.buttonFile .fileInput {
    position: absolute;
    opacity: 0;
    -moz-appearance: none;
    appearance: none;
    -webkit-appearance: none;
    width: 0;
    height: 0
}

.buttonFile .form-assist-text .form-error-text {
    margin-top: 4px;
    font-size: 12px;
    line-height: 16px;
    color: #ef4444
}

.buttonFile .profileImageWrapper {
    position: relative;
    width: 72px;
    height: 72px
}

.buttonFile .profileImageWrapper .profileImage {
    width: 100%;
    height: 100%;
    border: 1px solid #2e2e2e;
    border-radius: 50px;
    -o-object-fit: cover;
    object-fit: cover
}

.buttonFile .profileImageWrapper .iconBox {
    position: absolute;
    bottom: 0;
    right: -16px;
    display: flex;
    align-items: center;
    justify-content: center;
    width: 32px;
    height: 32px;
    border-radius: 50px;
    background-color: #2e2e2e;
    box-shadow: 0 2px 8px rgba(0,0,0,.1)
}

.buttonFile .profileImageWrapper .profileIcon {
    font-size: 72px;
    color: #161616
}

.buttonFile .loadingState {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: #2e2e2e;
    opacity: .8;
    border-radius: 500px
}

.buttonFile:focus {
    outline: 1px solid #161616;
    outline-offset: 2px
}

.versionTabBar {
    width: 100%;
    height: 48px;
    background-color: #161616;
    border-bottom: 1px solid #2e2e2e
}

.versionTabBar .inner {
    position: relative;
    display: flex;
    align-items: center;
    gap: 16px;
    height: 100%;
    padding: 0 16px
}

.versionTabBar .inner .versionList {
    display: flex;
    justify-content: center;
    align-items: center
}

.versionTabBar .inner .versionList .listItem .versionName {
    display: flex;
    justify-content: center;
    align-items: center;
    width: 96px;
    height: 32px;
    font-size: 14px;
    line-height: 20px;
    color: #707070;
    transition: all .2s
}

@media screen and (min-width: 1024px) {
    .versionTabBar .inner .versionList .listItem .versionName:hover {
        background-color:#232323;
        border-radius: 4px;
        transition: all .2s
    }
}

.versionTabBar .inner .versionList .listItem .active {
    position: relative;
    font-weight: 700;
    color: #fff
}

.versionTabBar .inner .versionList .listItem .active:after {
    content: "";
    position: absolute;
    bottom: -8px;
    left: 50%;
    transform: translateX(-50%);
    -webkit-transform: translateX(-50%);
    -ms-transform: translateX(-50%);
    width: 96px;
    height: 2px;
    background-color: #fff;
    border-radius: 4px 4px 0 0
}

.normalTabBar {
    width: 100%;
    height: 48px;
    background-color: #161616;
    border-bottom: 1px solid #2e2e2e
}

.normalTabBar .inner {
    position: relative;
    display: flex;
    align-items: center;
    gap: 16px;
    height: 100%
}

.normalTabBar .inner .versionList {
    display: flex;
    justify-content: center;
    align-items: center
}

.normalTabBar .inner .versionList .listItem .listItemInner {
    display: flex;
    justify-content: center;
    align-items: center;
    width: 100%;
    height: 32px;
    padding: 0 8px;
    font-size: 14px;
    line-height: 20px;
    color: #707070;
    transition: all .2s
}

@media screen and (min-width: 1024px) {
    .normalTabBar .inner .versionList .listItem .listItemInner:hover {
        background-color:#232323;
        border-radius: 4px;
        transition: all .2s
    }
}

.normalTabBar .inner .versionList .listItem .active {
    position: relative;
    font-weight: 700;
    color: #fff
}

.normalTabBar .inner .versionList .listItem .active:after {
    content: "";
    position: absolute;
    bottom: -8px;
    left: 50%;
    transform: translateX(-50%);
    -webkit-transform: translateX(-50%);
    -ms-transform: translateX(-50%);
    width: 100%;
    height: 2px;
    background-color: #fff;
    border-radius: 4px 4px 0 0
}

.tabBar {
    position: sticky;
    top: 56px;
    left: 0;
    width: 100%;
    height: 56px;
    background-color: #161616;
    border-bottom: 1px solid #2e2e2e;
    z-index: 99
}

.tabBar .inner {
    position: relative;
    display: flex;
    align-items: center;
    gap: 16px;
    height: 100%;
    padding: 0 16px
}

.tabBar .inner .tabList,.tabBar .inner .tabList .listItem .listItemInner {
    display: flex;
    justify-content: center;
    align-items: center
}

.tabBar .inner .tabList .listItem .listItemInner {
    width: -moz-max-content;
    width: max-content;
    height: 32px;
    padding: 0 16px;
    font-size: 14px;
    line-height: 20px;
    color: #707070;
    transition: all .2s
}

@media screen and (min-width: 1024px) {
    .tabBar .inner .tabList .listItem .listItemInner:hover {
        background-color:#232323;
        border-radius: 4px;
        transition: all .2s
    }
}

.tabBar .inner .tabList .listItem .active {
    position: relative;
    font-weight: 700;
    color: #fff
}

.tabBar .inner .tabList .listItem .active:after {
    content: "";
    position: absolute;
    bottom: -12px;
    left: 50%;
    transform: translateX(-50%);
    -webkit-transform: translateX(-50%);
    -ms-transform: translateX(-50%);
    width: 100%;
    height: 2px;
    background-color: #fff;
    border-radius: 4px 4px 0 0
}

.filterBar {
    position: sticky;
    top: 56px;
    left: 0;
    width: 100%;
    height: 56px;
    background-color: #161616;
    border-bottom: 1px solid #2e2e2e;
    z-index: 99
}

.filterBar .inner {
    position: relative;
    display: flex;
    align-items: center;
    height: 100%;
    padding: 0 0 0 16px
}

.filterBar .inner .filterHeader {
    position: absolute;
    top: 50%;
    transform: translateY(-50%);
    -webkit-transform: translateY(-50%);
    -ms-transform: translateY(-50%);
    left: 16px;
    display: flex;
    align-items: center;
    gap: 6px;
    padding-right: 12px;
    margin-right: 12px;
    border-right: 1px solid #2e2e2e
}

.filterBar .inner .filterHeader .icon {
    fill: #7e7e7e
}

.filterBar .inner .filterHeader span {
    font-size: 14px;
    line-height: 20px;
    color: #7e7e7e
}

.filterBar .inner .filterListWrapper {
    position: relative;
    width: calc(100% - 94px);
    margin-left: 94px
}

.filterBar .inner .filterListWrapper:before {
    position: absolute;
    content: "";
    top: 0;
    left: 0;
    width: 16px;
    height: 100%;
    background: linear-gradient(90deg,#171717,hsla(0,0%,9%,0))
}

.filterBar .inner .filterListWrapper:after {
    position: absolute;
    content: "";
    top: 0;
    right: 0;
    width: 16px;
    height: 100%;
    background: linear-gradient(270deg,#171717,hsla(0,0%,9%,0))
}

.filterBar .inner .filterListWrapper .filterListBox {
    overflow: scroll;
    padding: 0 16px 0 0
}

.filterBar .inner .filterListWrapper .filterListBox .filterList {
    display: flex;
    align-items: center;
    gap: 8px;
    width: -moz-max-content;
    width: max-content;
    height: 48px;
    padding-left: 12px
}

.filterBar .inner .filterListWrapper .filterListBox .filterList .listItem {
    display: flex;
    align-items: center;
    gap: 4px;
    padding: 2px 2px 2px 12px;
    background-color: #232323;
    outline: 1px solid #2e2e2e;
    outline-offset: -1px;
    border-radius: 50px;
    overflow: hidden;
    box-sizing: border-box
}

.filterBar .inner .filterListWrapper .filterListBox .filterList .listItem span {
    font-size: 14px;
    line-height: 20px;
    color: #d4d4d4
}

.filterBar .inner .filterListWrapper .filterListBox .filterList .listItem button {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 28px;
    height: 28px;
    background-color: #232323;
    border-radius: 50px;
    transition: all .2s
}

@media screen and (min-width: 640px) {
    .filterBar .inner .filterListWrapper .filterListBox .filterList .listItem button:hover {
        background-color:#343434;
        transition: all .2s
    }
}

.filterBar .inner .filterListWrapper .filterListBox .filterList .listItem button .icon {
    color: #a0a0a0
}

.sidebar-segmented-control-wrapper {
    position: sticky;
    top: 56px;
    left: 0;
    z-index: 99
}

.sidebar-segmented-control-wrapper .sidebar-segmented-control {
    position: relative;
    display: flex;
    justify-content: space-between;
    background-color: #161616;
    padding: 8px;
    border-bottom: 1px solid #2e2e2e;
    width: 100%;
    height: 56px;
    margin: auto;
    overflow: hidden;
    cursor: pointer
}

.sidebar-segmented-control-wrapper .sidebar-segmented-control li {
    position: relative;
    color: #7e7e7e;
    font-size: 14px;
    line-height: 20px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    gap: 4px;
    align-items: center;
    width: 84px;
    padding: 2px;
    font-weight: 400;
    z-index: 2
}

.sidebar-segmented-control-wrapper .sidebar-segmented-control li a {
    display: flex;
    flex-direction: column;
    justify-content: center;
    gap: 4px;
    align-items: center;
    width: 100%;
    height: 100%
}

.sidebar-segmented-control-wrapper .sidebar-segmented-control li:hover {
    background-color: #232323;
    border-radius: 4px;
    transition: all .2s
}

.sidebar-segmented-control-wrapper .sidebar-segmented-control li:nth-child(2).active-segment~span {
    left: calc(33.3% + 4px)
}

.sidebar-segmented-control-wrapper .sidebar-segmented-control li:nth-child(3).active-segment~span {
    left: 66%
}

.sidebar-segmented-control-wrapper .sidebar-segmented-control li .segment-description {
    font-size: 10px;
    line-height: 12px
}

.sidebar-segmented-control-wrapper .sidebar-segmented-control .active-segment {
    transition: .2s ease;
    color: #fff;
    font-weight: 700
}

.sidebar-segmented-control-wrapper .sidebar-segmented-control span {
    position: absolute;
    width: 84px;
    height: 2px;
    background-color: #fff;
    bottom: 0;
    left: 8px;
    border-radius: 6px 6px 0 0;
    z-index: 1;
    transition: left .2s ease
}

.sidebar-segmented-control-wrapper .sidebar-segmented-control li:first-child.active-segment~span {
    left: 8px
}

.sidebar-segmented-control-wrapper .sidebar-segmented-control li:nth-child(2).active-segment~span {
    left: 33.3%
}

.sidebar-segmented-control-wrapper .sidebar-segmented-control li:nth-child(3).active-segment~span {
    left: 66.6%
}

.sidebar-segmented-control-wrapper-under-construction {
    position: sticky;
    top: 56px;
    left: 0;
    z-index: 99
}

.sidebar-segmented-control-wrapper-under-construction .sidebar-segmented-control {
    position: relative;
    display: flex;
    justify-content: space-between;
    background-color: #161616;
    padding: 8px;
    border-bottom: 1px solid #2e2e2e;
    width: 100%;
    height: 56px;
    margin: auto;
    overflow: hidden;
    cursor: pointer
}

.sidebar-segmented-control-wrapper-under-construction .sidebar-segmented-control li {
    width: 50%
}

.sidebar-segmented-control-wrapper-under-construction .sidebar-segmented-control li a {
    position: relative;
    color: #7e7e7e;
    font-size: 14px;
    line-height: 20px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    gap: 4px;
    align-items: center;
    width: 100%;
    padding: 2px;
    font-weight: 400;
    z-index: 2
}

.sidebar-segmented-control-wrapper-under-construction .sidebar-segmented-control li a:hover {
    background-color: #232323;
    border-radius: 4px;
    transition: all .2s
}

.sidebar-segmented-control-wrapper-under-construction .sidebar-segmented-control li a:first-child.active-segment~span {
    left: 8px
}

.sidebar-segmented-control-wrapper-under-construction .sidebar-segmented-control li a:nth-child(2).active-segment~span {
    left: 50%
}

.sidebar-segmented-control-wrapper-under-construction .sidebar-segmented-control li a .segment-description {
    font-size: 10px;
    line-height: 12px
}

.sidebar-segmented-control-wrapper-under-construction .sidebar-segmented-control .active-segment a {
    transition: .2s ease;
    color: #fff;
    font-weight: 700
}

.sidebar-segmented-control-wrapper-under-construction .sidebar-segmented-control span {
    position: absolute;
    width: calc(50% - 8px);
    height: 2px;
    background-color: #fff;
    bottom: 0;
    left: 8px;
    border-radius: 6px 6px 0 0;
    z-index: 1;
    transition: left .2s ease
}

.sidebar-segmented-control-wrapper-under-construction .sidebar-segmented-control li:first-child.active-segment~span {
    left: 8px
}

.sidebar-segmented-control-wrapper-under-construction .sidebar-segmented-control li:nth-child(2).active-segment~span {
    left: 33.3%
}

.sidebar-segmented-control-wrapper-under-construction .sidebar-segmented-control li:nth-child(3).active-segment~span {
    left: 66.6%
}

.componentsListWrapper .h2 {
    font-size: 20px;
    line-height: 28px;
    font-weight: 700
}

.componentsListWrapper .componentsList {
    display: grid;
    grid-template-columns: 1fr;
    gap: 32px
}

@media screen and (min-width: 1024px) {
    .componentsListWrapper .componentsList {
        grid-template-columns:1fr 1fr 1fr;
        -moz-column-gap: 16px;
        column-gap: 16px;
        row-gap: 32px
    }
}

@media screen and (min-width: 1536px) {
    .componentsListWrapper .componentsList {
        grid-template-columns:1fr 1fr 1fr 1fr
    }
}

.componentsListWrapper .componentsList .listItem .listItemInner .thumbnailWrapper {
    width: 100%;
    aspect-ratio: 1.91/1;
    background-color: #232323;
    border: 1px solid #232323;
    border-radius: 8px;
    overflow: hidden;
    transition: all .2s
}

.componentsListWrapper .componentsList .listItem .listItemInner .thumbnailWrapper .thumbnail {
    width: 100%;
    height: auto;
    transition: all .2s
}

.componentsListWrapper .componentsList .listItem .listItemInner .h3 {
    font-size: 16px;
    line-height: 24px;
    font-weight: 700
}

.componentsListWrapper .componentsList .listItem .listItemInner .p {
    font-size: 12px;
    line-height: 16px;
    color: #d4d4d4
}

.componentsListWrapper .componentsList .listItem .listItemInner:hover .thumbnailWrapper {
    border: 1px solid #2e2e2e;
    transition: all .2s
}

.componentsListWrapper .componentsList .listItem .listItemInner:hover .thumbnailWrapper .thumbnail {
    transform: scale(1.15);
    transition: all .2s
}

.toc .toc-list {
    display: flex;
    flex-direction: column;
    gap: 12px;
    border-left: 2px solid #232323
}

.toc .toc-list .toc-list-item {
    padding: 0 0 0 16px;
    margin-left: -2px;
    border-left: 2px solid #232323
}

.toc .toc-list .toc-list-item .toc-link {
    padding: 2px 0;
    color: #7e7e7e;
    transition: .2s;
    font-size: 14px;
    line-height: 20px
}

@media screen and (min-width: 640px) {
    .toc .toc-list .toc-list-item .toc-link:hover {
        color:#fff;
        transition: .2s
    }
}

.toc .toc-list .toc-list-item .is-active-link {
    color: #fff
}

.toc .toc-list .toc-list-item .node-name--H2 {
    font-weight: 700
}

.toc .toc-list .toc-list-item .toc-list {
    margin-left: -18px;
    padding-top: 12px
}

.toc .toc-list .toc-list-item .toc-list .toc-list-item {
    padding-left: 32px
}

.toc .toc-list .is-active-li {
    border-left: 2px solid #ec4899
}

.toc .hasParent {
    padding: 0 0 0 32px
}

.toc .hasParent .inPageLink {
    font-weight: 400;
    color: #7e7e7e
}

.toc .hasGrandParent {
    padding: 0 0 0 64px
}

.toc .hasGrandParent .inPageLink {
    font-weight: 400;
    color: #7e7e7e
}

.toc .hasGreatGrandParent {
    padding: 0 0 0 72px
}

.toc .hasGreatGrandParent .inPageLink {
    font-weight: 400;
    color: #7e7e7e
}

.localizedFlowsToc {
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 0;
    padding-left: 16px
}

.localizedFlowsToc:before {
    left: 0
}

.localizedFlowsToc:after,.localizedFlowsToc:before {
    content: "";
    position: absolute;
    top: 0;
    width: 24px;
    height: 100%;
    border-right: 1px solid #707070;
    border-left: 1px solid #707070
}

.localizedFlowsToc:after {
    left: 48px
}

.localizedFlowsToc .tocListItem {
    position: relative;
    z-index: 2;
    background-color: #161616;
    padding: 6px 0
}

.localizedFlowsToc .tocListItem:before {
    content: "";
    position: absolute;
    top: 0;
    left: -16px;
    width: 12px;
    height: 50%;
    border-bottom: 1px solid #707070
}

.localizedFlowsToc .tocListItem .tocLink {
    display: flex;
    align-items: center;
    gap: 8px;
    padding: 2px 0;
    color: #7e7e7e;
    transition: .2s;
    font-size: 14px;
    line-height: 20px
}

.localizedFlowsToc .tocListItem .tocLink .icon {
    opacity: .5;
    min-width: 18px
}

@media screen and (min-width: 640px) {
    .localizedFlowsToc .tocListItem .tocLink:hover {
        color:#fff;
        transition: .2s
    }

    .localizedFlowsToc .tocListItem .tocLink:hover .icon {
        opacity: 1;
        transition: .2s
    }

    .localizedFlowsToc .tocListItem .tocLink:hover .screensLengthInfo {
        color: #7e7e7e
    }
}

.localizedFlowsToc .tocListItem .tocLink .screensLengthInfo {
    display: flex;
    justify-content: center;
    align-items: flex-end;
    align-items: center;
    color: #7e7e7e;
    border-radius: 4px;
    font-size: 12px;
    line-height: 16px
}

.localizedFlowsToc .tocListItem .activeLink {
    color: #fff
}

.localizedFlowsToc .tocListItem .activeLink .icon {
    opacity: 1
}

.localizedFlowsToc .tocListItem .is-active-link {
    color: #fff
}

.localizedFlowsToc .tocListItem .node-name--H2 {
    font-weight: 700
}

.localizedFlowsToc .tocListItem .toc-list {
    margin-left: -18px;
    padding-top: 12px
}

.localizedFlowsToc .tocListItem .toc-list .toc-list-item {
    padding-left: 32px
}

.localizedFlowsToc .notHasParent {
    position: relative
}

.localizedFlowsToc .hasParent {
    margin-left: 24px
}

.localizedFlowsToc .hasGrandParent {
    margin-left: 48px
}

.localizedFlowsToc .hasGreatGrandParent {
    margin-left: 72px
}

.dropdownButtonMd {
    display: flex;
    align-items: center;
    justify-content: center;
    height: 40px;
    width: 40px;
    background-color: rgba(50,50,50,.5);
    border: 1px solid hsla(0,0%,100%,.1);
    backdrop-filter: blur(40px);
    -webkit-backdrop-filter: blur(40px);
    border-radius: 100px;
    transition: .2s
}

.dropdownButtonMd:active {
    transform: scale(.96)
}

.dropdownButtonMd:hover {
    background-color: rgba(75,75,75,.5);
    transition: .2s
}

.dropdownButtonMd:disabled:hover {
    background-color: rgba(50,50,50,.5)
}

.dropdownButtonSm {
    display: flex;
    align-items: center;
    justify-content: center;
    height: 32px;
    width: 32px
}

.dropdownMenuWrapper .menuList {
    display: flex;
    align-items: center;
    gap: 8px;
    padding: 8px
}

.dropdownMenuWrapper .menuList .userName {
    font-size: 16px;
    line-height: 24px;
    font-weight: 700
}

.dropdownMenuWrapper .menuButton {
    display: flex;
    align-items: center;
    gap: 8px;
    width: 100%;
    padding: 10px;
    border-radius: 8px;
    transition: all .2s
}

.dropdownMenuWrapper .menuButton .buttonText {
    font-size: 14px;
    line-height: 20px
}

.dropdownMenuWrapper .menuButtonDanger {
    display: flex;
    align-items: center;
    gap: 8px;
    width: 100%;
    padding: 10px;
    border-radius: 8px;
    transition: all .2s
}

.dropdownMenuWrapper .menuButtonDanger .icon {
    color: #ef4444
}

.dropdownMenuWrapper .menuButtonDanger .buttonText {
    font-size: 14px;
    line-height: 20px;
    color: #ef4444
}

.dropdownMenuWrapper .menuButton[data-active] {
    display: flex;
    align-items: center;
    gap: 8px;
    width: 100%;
    padding: 10px;
    border-radius: 8px;
    background-color: hsla(0,0%,100%,.1);
    transition: all .2s
}

.dropdownMenuWrapper .menuButton[data-active] .buttonText {
    font-size: 14px;
    line-height: 20px
}

.dropdownMenuWrapper .menuButtonDanger[data-active] {
    display: flex;
    align-items: center;
    gap: 8px;
    width: 100%;
    padding: 10px;
    border-radius: 8px;
    background-color: rgba(239,68,68,.2);
    transition: all .2s
}

.dropdownMenuWrapper .menuButtonDanger[data-active] .icon {
    color: #ef4444
}

.dropdownMenuWrapper .menuButtonDanger[data-active] .buttonText {
    font-size: 14px;
    line-height: 20px;
    color: #ef4444
}

.dropdownMenuWrapper .avatarButton {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 32px;
    height: 32px;
    border: 1px solid #2e2e2e;
    border-radius: 50px;
    overflow: hidden
}

.dropdownMenuWrapper .avatarButton .skeltonAvatar {
    width: 100%;
    height: 100%;
    background: #232323;
    position: relative;
    border-radius: 50px;
    overflow: hidden;
    cursor: zoom-in
}

.dropdownMenuWrapper .avatarButton .skeltonAvatar:before {
    content: "";
    display: block;
    height: 100%;
    width: 100%;
    background: linear-gradient(90deg,transparent,rgba(80,80,80,.1),transparent);
    position: absolute;
    top: 0;
    left: 0;
    animation: skeleton-animation 1.2s linear infinite
}

.dropdownMenuWrapper .avatarButton .avatarImg {
    width: 100%;
    height: 100%;
    -o-object-fit: cover;
    object-fit: cover
}

.dropdownMenuWrapper .subscribed {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 36px;
    height: 36px;
    background: linear-gradient(138deg,#f957dc 37.44%,#72aeff 100.06%);
    border-radius: 50px
}

.popupInner {
    position: relative;
    padding: 0;
    width: 100%
}

.popupInner .popupHeader {
    position: sticky;
    top: 0;
    left: 0;
    width: 100%;
    background-color: #232323;
    border-bottom: 1px solid #2e2e2e
}

.popupInner .popupHeader .inner {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 100%;
    height: 56px;
    padding: 0 16px
}

.popupInner .popupHeader .inner .closeButton {
    position: absolute;
    top: 12px;
    left: 16px
}

.popupInner .popupHeader .inner .popupTitle {
    font-size: 16px;
    line-height: 24px;
    font-weight: 700;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis
}

.popupInner .popupHeader .inner .favoriteButtonWrapper {
    position: absolute;
    top: 12px;
    right: 16px
}

.popupInner .popupContent {
    padding: 0 24px 24px
}

.popupInner .popupContent .buttonWrapper {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 16px
}

.loaderBox {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 20px;
    height: 20px
}

.loaderBox .loader {
    width: 16px;
    height: 16px;
    border: 2px solid #d4d4d4;
    border-bottom-color: transparent;
    border-radius: 50%;
    display: inline-block;
    box-sizing: border-box;
    animation: rotation 1s linear infinite
}

@keyframes rotation {
    0% {
        transform: rotate(0deg)
    }

    to {
        transform: rotate(1turn)
    }
}

.tableWrapper {
    width: 100%;
    height: 100%
}

.tableGrid {
    height: 100%
}

.tableGrid .tableHeader {
    position: sticky;
    top: 40px;
    left: 0;
    width: 100%;
    height: 40px;
    background-color: #232323;
    color: #7e7e7e
}

.tableGrid .tableHeader,.tableGrid .tableRow {
    display: flex;
    align-items: center;
    border-bottom: 1px solid #2e2e2e
}

.tableGrid .tableRow {
    gap: 16px;
    min-width: 100%;
    width: -moz-max-content;
    width: max-content;
    padding: 12px 16px
}

.tableGrid .tableRow .tabletCell {
    font-size: 14px;
    line-height: 20px;
    color: #7e7e7e;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap
}

.tableGrid .tableRow .tabletCell .appInfo {
    display: flex;
    align-items: center;
    gap: 16px;
    color: #fff
}

.tableGrid .tableRow .tabletCell .appInfo:hover .appTitle {
    text-decoration: underline
}

.tableGrid .tableRow .tabletCell .appInfo .appIcon {
    width: 40px;
    height: 40px;
    -o-object-fit: cover;
    object-fit: cover;
    border-radius: 20%
}

.tableGrid .tableRow .tabletCell .appInfo .discriptionBox {
    width: 168px
}

.tableGrid .tableRow .tabletCell .appInfo .discriptionBox .appTitle {
    font-size: 16px;
    line-height: 24px;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap
}

.tableGrid .tableRow .tabletCell .appInfo .discriptionBox .appDescription {
    font-size: 12px;
    line-height: 16px;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
    color: #7e7e7e
}

.tableGrid .tableRow .tabletCell .tableLink:hover {
    color: #fff;
    text-decoration: underline
}

.tableGrid .tableRow .cellsm {
    width: 56px
}

.tableGrid .tableRow .cellNormal {
    width: 144px
}

.tableGrid .tableRow .cellLg {
    width: 224px
}

.tableFooter {
    position: fixed;
    bottom: 0;
    right: 0;
    display: flex;
    align-items: center;
    gap: 16px;
    width: calc(100% - 328px);
    height: 40px;
    padding: 0 16px;
    background-color: #232323;
    border-top: 1px solid #2e2e2e
}

.tableFooter .pageDestination {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 32px
}

.tableFooter .pageDestination,.tableFooter .totalRecords {
    font-size: 14px;
    line-height: 20px;
    color: #7e7e7e
}

.pagination {
    display: flex;
    align-items: center;
    gap: 16px;
    width: -moz-max-content;
    width: max-content;
    height: 40px;
    margin: auto;
    padding: 0 16px
}

.pagination .pageDestination {
    position: relative;
    display: flex;
    align-items: center;
    gap: 6px
}

.pagination .pageDestination .singleSelect {
    width: 56px;
    height: 32px;
    padding: 5px 24px 5px 12px;
    font-size: 14px;
    line-height: 20px;
    border: 1px solid #2e2e2e;
    border-radius: 6px;
    cursor: pointer
}

.pagination .pageDestination .icon {
    position: absolute;
    top: 8px;
    left: 36px;
    pointer-events: none
}

.pagination .pageDestination .totalPages {
    font-size: 14px;
    line-height: 20px;
    color: #7e7e7e
}

.pagination .totalRows {
    font-size: 12px;
    line-height: 16px
}

.localHeader {
    position: fixed;
    top: 56px;
    width: calc(100% - 56px);
    height: 40px;
    z-index: 99
}

.localHeader .inner {
    display: flex;
    align-items: center;
    justify-content: space-between;
    width: 100%;
    height: 100%;
    padding: 0 16px;
    background-color: #232323;
    border-bottom: 1px solid #2e2e2e
}

.localHeader .inner .titleWrapper {
    display: flex;
    align-items: center;
    gap: 8px
}

.localHeader .inner .titleWrapper .iconWrapper {
    width: 24px;
    height: 24px;
    border-radius: 4px;
    overflow: hidden
}

.localHeader .inner .titleWrapper .iconWrapper .icon {
    width: 100%;
    height: 100%;
    -o-object-fit: cover;
    object-fit: cover
}

.localHeader .inner .titleWrapper .title {
    font-size: 12px;
    line-height: 16px
}

.localHeader .inner .controlsWrapper {
    display: flex;
    align-items: center;
    gap: 32px
}

.label,.localHeader .inner .controlsWrapper .status {
    font-size: 12px;
    line-height: 16px
}

.label {
    display: flex;
    align-items: center;
    gap: 8px;
    width: -moz-max-content;
    width: max-content;
    padding: 4px 8px;
    border-radius: 50px
}

.label .statusIcon {
    width: 8px;
    height: 8px;
    border-radius: 50px
}

.draft {
    background-color: #2e2e2e;
    color: #7e7e7e
}

.draft .statusIcon {
    background-color: #7e7e7e
}

.published {
    background-color: #14532d;
    color: #86efac
}

.published .statusIcon {
    background-color: #86efac
}

.drawerHeader {
    border-bottom: 1px solid #2e2e2e
}

.drawerHeader .inner {
    display: flex;
    align-items: center;
    width: 100%;
    height: 56px;
    padding: 0 16px
}

.drawerHeader .inner .drawerTitle {
    font-size: 16px;
    line-height: 24px
}

.drawerSection {
    padding: 16px;
    height: calc(95vh - 56px)
}

.drawerSection .form {
    display: flex;
    flex-direction: column;
    gap: 16px;
    padding-bottom: 72px
}

.drawerSection .form .sectionForm {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding-bottom: 16px;
    border-bottom: 1px solid #2e2e2e
}

.drawerSection .form .sectionForm .titleWrapper {
    display: flex;
    gap: 8px
}

.drawerSection .form .sectionForm .titleWrapper .textInputWrapper:first-child {
    width: 80px
}

.drawerSection .form .sectionForm .titleWrapper .textInputWrapper:last-child {
    width: 240px
}

.drawerSection .form .sectionForm .controlWrapper {
    display: flex;
    gap: 16px;
    align-items: last baseline
}

.drawerSection .form .thmlailList {
    display: flex;
    gap: 16px
}

.drawerSection .form .thmlailList .listItem {
    position: relative;
    width: 16%;
    border: 1px dashed #2e2e2e;
    border-radius: 16px;
    cursor: pointer
}

.drawerSection .form .thmlailList .listItem:after {
    content: "+";
    font-size: 24px;
    line-height: 32px;
    color: #707070;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%,-50%);
    -webkit-transform: translate(-50%,-50%);
    -ms-transform: translate(-50%,-50%)
}

.drawerSection .form .thmlailList .listItem .screen {
    aspect-ratio: 390/844;
    border-radius: 12px
}

.drawerSection .form .floatSection {
    position: fixed;
    bottom: 0;
    right: 0;
    display: flex;
    align-items: center;
    justify-content: space-between;
    width: 100%;
    height: 56px;
    padding: 0 16px;
    background-color: #232323;
    border-top: 1px solid #2e2e2e
}

.drawerSection .form .floatSection .flexWrapper {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 16px
}

.switchBox {
    display: flex;
    align-items: center;
    gap: 8px
}

.switchBox span {
    font-size: 14px;
    line-height: 20px
}

.switchBox .switch {
    position: relative;
    display: flex;
    width: 52px;
    height: 32px;
    padding: 2px;
    background-color: #2e2e2e;
    border-radius: 50px;
    overflow: hidden;
    transition: .2s ease
}

.switchBox .switch span {
    position: absolute;
    top: 2px;
    bottom: 2px;
    left: 2px;
    width: 28px;
    background-color: #fff;
    border-radius: 50px;
    box-shadow: 0 2px 4px rgba(0,0,0,.1);
    transition: .2s ease;
    z-index: 1
}

.switchBox .activeSwitch {
    background-color: #ec4899
}

.switchBox .activeSwitch span {
    left: 22px
}

.separatedSection {
    display: grid;
    grid-template-columns: 1fr 1fr;
    border-top: 1px solid #2e2e2e
}

.board .sections {
    display: flex;
    flex-direction: column;
    gap: 16px
}

.board .sections .section {
    padding: 16px;
    background-color: #232323;
    border-radius: 6px
}

.board .sections .section .sectionHeader {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding-bottom: 16px;
    border-bottom: 1px solid #2e2e2e
}

.board .sections .section .sectionHeader .titleWrapper {
    display: flex;
    align-items: center;
    gap: 8px
}

.board .sections .section .sectionHeader .titleWrapper .label {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 32px;
    height: 32px;
    border-radius: 4px;
    background-color: #2e2e2e;
    font-size: 14px;
    line-height: 20px
}

.board .sections .section .sectionHeader .titleWrapper .title {
    font-weight: 700
}

.board .sections .section .sectionHeader .controlWrapper {
    display: flex;
    gap: 8px
}

.board .sections .section .screenGridListWrapperWeb .screenGridList {
    grid-template-columns: 1fr 1fr 1fr 1fr
}

.board .sections .section .screenGridListWrapperWeb .listItem {
    background-color: #232323
}

.board .sections .section .screenGridListWrapperWeb .listItem .screenWrapper {
    aspect-ratio: 1470/956;
    border-radius: 8px
}

.board .sections .section .screenGridListWrapperWeb .listItem .screen {
    width: 100%;
    height: 100%
}

.board .sections .section .screenGridListWrapperMobile .screenGridList {
    grid-template-columns: 1fr 1fr 1fr 1fr 1fr 1fr
}

.board .sections .section .screenGridListWrapperMobile .listItem {
    background-color: #232323
}

.board .sections .section .screenGridListWrapperMobile .listItem .screenWrapper {
    aspect-ratio: 390/844;
    border-radius: 8px
}

.board .sections .section .screenGridListWrapperMobile .listItem .screen {
    width: 100%;
    height: 100%
}

.board .sections .hasParent {
    margin-left: 32px
}

.board .sections .hasGrandParent {
    margin-left: 64px
}

.board .sections .hasGreatGrandParent {
    margin-left: 96px
}

.queuedScreensContainer {
    position: fixed;
    bottom: 0;
    right: 0;
    width: calc(100vw - 50% - 32px);
    height: calc(100vh - 56px);
    overflow-y: scroll;
    border-left: 1px solid #2e2e2e
}

.queuedScreensContainer .queuedScreensInner {
    height: -moz-max-content;
    height: max-content;
    background-color: #232323
}

.queuedScreensContainer .queuedScreensInner .toolbar {
    position: fixed;
    bottom: 16px;
    right: 32px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 16px;
    width: 400px;
    padding: 8px;
    box-shadow: 0 4px 24px rgba(0,0,0,.25);
    border-radius: 50px;
    background-color: #232323;
    border-bottom: 1px solid #2e2e2e;
    z-index: 999
}

.queuedScreensContainer .queuedScreensInner .toolbar .leftSection {
    display: flex;
    align-items: center;
    gap: 8px
}

.queuedScreensContainer .queuedScreensInner .toolbar .leftSection .currentSituation {
    font-size: 14px;
    line-height: 20px;
    color: #fff
}

.queuedScreensContainer .queuedScreensInner .toolbar .rightSection {
    display: flex;
    align-items: center;
    gap: 8px
}

.queuedScreensContainer .queuedScreensInner .toolbar .rightSection .dropdownButton {
    font-weight: 700
}

.queuedScreensContainer .queuedScreensInner .screenGridListWrapper .screenGridList {
    grid-template-columns: 1fr 1fr 1fr 1fr 1fr 1fr 1fr
}

.queuedScreensContainer .queuedScreensInner .screenGridListWrapperWeb .screenGridList {
    grid-template-columns: 1fr 1fr 1fr 1fr
}

.queuedScreensContainer .queuedScreensInner .screenGridListWrapperWeb .screenWrapper {
    aspect-ratio: 1470/956;
    border-radius: 8px
}

.queuedScreensContainer .queuedScreensInner .screenGridListWrapperWeb .screenWrapper .screenHeader {
    padding: 4px
}

.flowPatternPopup {
    width: 100%;
    height: 90svh;
    overflow: scroll
}

.flowPatternPopup .flowPatternPopUpInner {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr 1fr 1fr 1fr
}

.flowPatternPopup .flowPatternPopUpInner .componentsParent {
    font-size: 14px;
    line-height: 20px;
    font-weight: 700;
    margin-top: 16px
}

.flowPatternPopup .flowPatternPopUpInner .floatButton {
    position: sticky;
    bottom: 0;
    right: 0
}

.flowPatternPopup .flowPatternPopUpInner .borderTop {
    border-top: 1px solid #707070
}

.addSectionButton {
    position: relative;
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    gap: 8px;
    width: 100%;
    margin-top: 20px;
    padding: 20px
}

.addSectionButton span {
    font-size: 16px;
    line-height: 24px;
    color: #707070
}

.addSectionButton:before {
    content: "";
    background-image: linear-gradient(90deg,#404040,#404040 6px,transparent 0,transparent 12px),linear-gradient(90deg,#404040,#404040 6px,transparent 0,transparent 12px),linear-gradient(180deg,#404040,#404040 6px,transparent 0,transparent 12px),linear-gradient(180deg,#404040,#404040 6px,transparent 0,transparent 12px);
    background-size: 12px 1px,12px 1px,1px 12px,1px 12px;
    background-position: 0 0,0 100%,0 0,100% 0;
    background-repeat: repeat-x,repeat-x,repeat-y,repeat-y;
    position: absolute;
    top: 0;
    bottom: 0;
    left: 0;
    right: 0;
    pointer-events: none
}

.mainDialogBackground {
    position: fixed;
    top: 0;
    right: 0;
    bottom: 0;
    left: 0;
    z-index: 8999;
    background-color: rgba(0,0,0,.5)
}

.mainDialog {
    width: 95%;
    height: 95vh;
    overflow: scroll;
    background-color: #232323;
    border: 1px solid #2e2e2e;
    z-index: 9000;
    border-radius: 16px
}

.mainDialog .drawerHeader {
    border-bottom: 1px solid #2e2e2e
}

.mainDialog .drawerHeader .inner {
    display: flex;
    align-items: center;
    width: 100%;
    height: 56px;
    padding: 0 16px
}

.mainDialog .drawerHeader .inner .drawerTitle {
    font-size: 16px;
    line-height: 24px
}

.mainDialog .drawerSection {
    padding: 16px
}

.mainDialog .drawerSection .form {
    position: relative;
    display: flex;
    flex-direction: column;
    gap: 16px;
    padding-bottom: 0
}

.mainDialog .drawerSection .form .sectionForm {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding-bottom: 16px;
    border-bottom: 1px solid #2e2e2e
}

.mainDialog .drawerSection .form .sectionForm .titleWrapper {
    display: flex;
    gap: 8px
}

.mainDialog .drawerSection .form .sectionForm .titleWrapper .textInputWrapper:first-child {
    width: 80px
}

.mainDialog .drawerSection .form .sectionForm .titleWrapper .textInputWrapper:last-child {
    width: 240px
}

.mainDialog .drawerSection .form .sectionForm .controlWrapper {
    display: flex;
    gap: 16px;
    align-items: last baseline
}

.mainDialog .drawerSection .form .screenGridListWrapper {
    width: 100%
}

.mainDialog .drawerSection .form .screenGridListWrapper .screenGridList {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr 1fr 1fr
}

.mainDialog .drawerSection .form .screenGridListWrapper .screenGridList .listItem {
    background-color: #161616
}

.mainDialog .drawerSection .form .screenGridListWrapper .screenGridList .listItem .screenWrapper {
    position: relative
}

.mainDialog .drawerSection .form .screenGridListWrapper .screenGridList .listItem .screenWrapper .screenInfo {
    position: absolute;
    bottom: 0;
    left: 0;
    width: 100%;
    padding: 8px;
    background-color: rgba(0,0,0,.75);
    border-radius: 0 0 12px 12px
}

.mainDialog .drawerSection .form .screenGridListWrapper .screenGridList .listItem .screenWrapper .screenInfo .position {
    font-weight: 700
}

.mainDialog .drawerSection .form .screenGridListWrapper .webScreenGridListWrapper .screenGridList {
    grid-template-columns: 1fr 1fr 1fr 1fr
}

.mainDialog .drawerSection .form .screenGridListWrapper .webScreenGridListWrapper .listItem {
    background-color: #232323
}

.mainDialog .drawerSection .form .screenGridListWrapper .webScreenGridListWrapper .listItem .screenWrapper {
    aspect-ratio: 1470/956;
    border-radius: 8px
}

.mainDialog .drawerSection .form .screenGridListWrapper .webScreenGridListWrapper .listItem .screenWrapper .screen {
    width: 100%;
    height: 100%
}

.mainDialog .drawerSection .form .floatSection {
    position: sticky;
    bottom: 0;
    right: 0;
    display: flex;
    align-items: center;
    justify-content: space-between;
    width: 100%;
    height: 56px;
    padding: 16px;
    background-color: #232323;
    border-top: 1px solid #2e2e2e
}

.mainDialog .drawerSection .form .floatSection .flexWrapper {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 16px;
    width: 50%
}

.nestedDialogWrapper {
    z-index: 9002
}

.nestedDialogWrapper .nestedDialogBackground {
    position: fixed;
    top: 0;
    right: 0;
    bottom: 0;
    left: 0;
    background-color: rgba(0,0,0,.5)
}

.nestedDialogWrapper .nestedDialog {
    width: 90%;
    height: 95vh;
    padding: 16px;
    overflow: scroll;
    background-color: #232323;
    border: 1px solid #2e2e2e;
    z-index: 9000;
    border-radius: 16px
}

.nestedDialogWrapper .nestedDialog .sectionForm {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding-bottom: 16px;
    border-bottom: 1px solid #2e2e2e
}

.nestedDialogWrapper .nestedDialog .sectionForm .titleWrapper {
    display: flex;
    gap: 8px
}

.nestedDialogWrapper .nestedDialog .sectionForm .titleWrapper .textInputWrapper {
    width: 80px
}

.nestedDialogWrapper .nestedDialog .sectionForm .controlWrapper {
    display: flex;
    gap: 16px;
    align-items: last baseline
}

.nestedDialogWrapper .nestedDialog .screenComponentEditor {
    align-items: flex-start;
    display: flex;
    gap: 32px
}

.nestedDialogWrapper .nestedDialog .screenComponentEditor .buttonScreen {
    display: block;
    width: -moz-max-content;
    width: max-content;
    padding-right: 16px;
    cursor: pointer
}

.nestedDialogWrapper .nestedDialog .screenComponentEditor .buttonScreen .fileInput {
    position: absolute;
    opacity: 0;
    -moz-appearance: none;
    appearance: none;
    -webkit-appearance: none;
    width: 0;
    height: 0
}

.nestedDialogWrapper .nestedDialog .screenComponentEditor .buttonScreen .form-assist-text .form-error-text {
    margin-top: 4px;
    font-size: 12px;
    line-height: 16px;
    color: #ef4444
}

.nestedDialogWrapper .nestedDialog .screenComponentEditor .buttonScreen .singleScreenWrapper {
    position: relative;
    width: 400px;
    height: auto
}

.nestedDialogWrapper .nestedDialog .screenComponentEditor .buttonScreen .singleScreenWrapper .screen {
    width: 100%;
    height: auto;
    max-height: 560px;
    border: 1px solid #2e2e2e;
    -o-object-fit: contain;
    object-fit: contain
}

.nestedDialogWrapper .nestedDialog .screenComponentEditor .buttonScreen .singleScreenWrapper .iconBox {
    position: absolute;
    bottom: 0;
    right: -16px;
    display: flex;
    align-items: center;
    justify-content: center;
    width: 32px;
    height: 32px;
    border-radius: 50px;
    background-color: #2e2e2e;
    box-shadow: 0 2px 8px rgba(0,0,0,.1)
}

.nestedDialogWrapper .nestedDialog .screenComponentEditor .buttonScreen .singleScreenWrapper .profileIcon {
    font-size: 72px;
    color: #161616
}

.nestedDialogWrapper .nestedDialog .screenComponentEditor .buttonScreen:focus {
    outline: 1px solid #161616;
    outline-offset: 2px
}

.nestedDialogWrapper .nestedDialog .screenComponentEditor .componentsParentWrapper {
    display: flex
}

.nestedDialogWrapper .nestedDialog .screenComponentEditor .componentsParentWrapper .categoryList {
    width: 224px
}

.nestedDialogWrapper .nestedDialog .floatSection {
    position: fixed;
    bottom: 0;
    right: 0;
    display: flex;
    align-items: center;
    justify-content: space-between;
    width: 100%;
    height: 56px;
    padding: 0 16px;
    pointer-events: none;
    border-top: 1px solid #2e2e2e
}

.nestedDialogWrapper .nestedDialog .floatSection * {
    pointer-events: all
}

.nestedDialogWrapper .nestedDialog .floatSection .flexWrapper {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 16px;
    width: 50%
}

.thumbnailListWrapper .screenGridList {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr 1fr 1fr;
    gap: 4px
}

.thumbnailListWrapper .listItem {
    background-color: #232323
}

.thumbnailListWrapper .listItem .screenWrapper {
    aspect-ratio: 390/844;
    border-radius: 8px
}

.thumbnailListWrapper .listItem .screen {
    -o-object-fit: contain;
    object-fit: contain
}

.boardHeader {
    display: flex;
    justify-content: space-between;
    background-color: #232323;
    padding: 8px 16px
}

.boardHeader .title-box {
    display: flex;
    align-items: center;
    gap: 8px;
    font-size: 14px;
    line-height: 20px;
    font-weight: 700
}

.boardHeader .title-box img {
    width: 28px;
    height: 28px;
    border-radius: 6px
}

.controlHeader {
    top: 56px;
    left: 56px;
    display: flex;
    justify-content: space-between;
    padding-bottom: 16px;
    margin-bottom: 16px;
    border-bottom: 1px solid #232323
}

.screenListWrapperMobile .screenList {
    display: grid;
    grid-template-columns: minmax(calc(14.28% - 12px),calc(14.28% - 12px)) minmax(calc(14.28% - 12px),calc(14.28% - 12px)) minmax(calc(14.28% - 12px),calc(14.28% - 12px)) minmax(calc(14.28% - 12px),calc(14.28% - 12px)) minmax(calc(14.28% - 12px),calc(14.28% - 12px)) minmax(calc(14.28% - 12px),calc(14.28% - 12px));
    gap: 16px
}

.screenListWrapperMobile .screenList .listItem .screenWrapper {
    position: relative;
    width: 100%;
    aspect-ratio: 390/844;
    background-color: #232323;
    outline: 1px solid #232323;
    border-radius: 10%/4.7%;
    overflow: hidden;
    cursor: zoom-in;
    transition: .2s
}

.screenListWrapperMobile .screenList .listItem .screenWrapper .screen {
    width: 100%;
    border-radius: 10%/4.7%
}

.screenListWrapperMobile .screenList .listItem .screenWrapper:has(input[type=checkbox]:checked) {
    outline: 2px solid #ec4899;
    outline-offset: 2px;
    transition: .2s
}

.screenListWrapperMobile .screenList .listItem .screenWrapper .screenHeader {
    display: none
}

@media screen and (min-width: 1024px) {
    .screenListWrapperMobile .screenList .listItem .screenWrapper .screenHeader {
        position:absolute;
        top: 0;
        left: 0;
        display: flex;
        align-items: flex-end;
        justify-content: space-between;
        width: 100%;
        padding: 12px 12px 96px;
        background: linear-gradient(0deg,transparent,rgba(0,0,0,.5) 50%,rgba(0,0,0,.95));
        pointer-events: none;
        opacity: 0
    }

    .screenListWrapperMobile .screenList .listItem .screenWrapper .screenHeader * {
        pointer-events: all
    }

    .screenListWrapperMobile .screenList .listItem .screenWrapper .screenHeader>.inner {
        display: flex;
        align-items: center;
        justify-content: flex-end;
        width: 100%
    }

    .screenListWrapperMobile .screenList .listItem .screenWrapper .screenFooter {
        position: absolute;
        bottom: 0;
        left: 0;
        display: flex;
        align-items: flex-end;
        justify-content: space-between;
        width: 100%;
        padding: 96px 12px 12px;
        background: linear-gradient(0deg,rgba(0,0,0,.95),rgba(0,0,0,.5) 50%,transparent);
        pointer-events: none;
        opacity: 0
    }
}

@media screen and (min-width: 1024px)and (min-width:1280px) {
    .screenListWrapperMobile .screenList .listItem .screenWrapper .screenFooter {
        padding:96px 16px 16px
    }
}

@media screen and (min-width: 1024px) {
    .screenListWrapperMobile .screenList .listItem .screenWrapper .screenFooter * {
        pointer-events:all
    }

    .screenListWrapperMobile .screenList .listItem .screenWrapper .screenFooter .favoriteButtonWrapper {
        display: flex;
        justify-content: flex-end;
        gap: 8px;
        width: 100%;
        pointer-events: all
    }
}

@media screen and (min-width: 1024px)and (min-width:1280px) {
    .screenListWrapperMobile .screenList .listItem .screenWrapper .screenFooter .favoriteButtonWrapper {
        gap:12px
    }
}

@media screen and (min-width: 1024px) {
    .screenListWrapperMobile .screenList .listItem .screenWrapper .screenFooter .favoriteButtonWrapper .favoriteButton {
        padding:0 9px;
        background-color: hsla(0,0%,100%,.15);
        border: 1px solid hsla(0,0%,100%,0);
        backdrop-filter: blur(16px) saturate(180%);
        -webkit-backdrop-filter: blur(25px) saturate(180%)
    }

    .screenListWrapperMobile .screenList .listItem .screenWrapper .screenFooter .favoriteButtonWrapper .favoriteButton:hover {
        background-color: hsla(0,0%,100%,.25)
    }

    .screenListWrapperMobile .screenList .listItem .screenWrapper .screenFooter .favoriteButtonWrapper .favoriteButton .buttonText {
        display: none
    }

    .screenListWrapperMobile .screenList .listItem .screenWrapper .screenFooter .favoriteButtonWrapper .dropdownButton {
        padding: 0 9px;
        background-color: hsla(0,0%,100%,.15);
        border: 1px solid hsla(0,0%,100%,0);
        backdrop-filter: blur(16px) saturate(180%);
        -webkit-backdrop-filter: blur(25px) saturate(180%)
    }

    .screenListWrapperMobile .screenList .listItem .screenWrapper .screenFooter .favoriteButtonWrapper .dropdownButton:hover {
        background-color: hsla(0,0%,100%,.25)
    }

    .screenListWrapperMobile .screenList .listItem .screenWrapper .screenFooter .favoriteButtonWrapper .dropdownButton .buttonText,.screenListWrapperMobile .screenList .listItem .screenWrapper .screenFooter .favoriteButtonWrapper .dropdownButton .proLabel {
        display: none
    }

    .screenListWrapperMobile .screenList .listItem .screenWrapper:focus .screenFooter,.screenListWrapperMobile .screenList .listItem .screenWrapper:focus .screenHeader,.screenListWrapperMobile .screenList .listItem .screenWrapper:hover .screenFooter,.screenListWrapperMobile .screenList .listItem .screenWrapper:hover .screenHeader {
        opacity: 1
    }
}

.screenListWrapperMobile .screenList .listItem .appInfo {
    display: flex;
    align-items: center;
    gap: 8px;
    width: 100%;
    pointer-events: all
}

.screenListWrapperMobile .screenList .listItem .appInfo:hover {
    cursor: pointer
}

.screenListWrapperMobile .screenList .listItem .appInfo:hover .appTitle {
    text-decoration: underline
}

.screenListWrapperMobile .screenList .listItem .appInfo .appIcon {
    width: 28px;
    height: 28px;
    border-radius: 22.5%;
    overflow: hidden;
    background-color: #232323;
    outline: 1px solid #232323
}

.screenListWrapperMobile .screenList .listItem .appInfo .appTexts {
    width: calc(100% - 36px)
}

.screenListWrapperMobile .screenList .listItem .appInfo .appTexts .appTitle {
    font-size: 14px;
    line-height: 20px;
    font-weight: 700;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis
}

.screenListWrapperMobile .screenList .listItem .screenAdBox {
    aspect-ratio: 390/844;
    padding: 16px;
    border-radius: 10%/4.7%;
    background-color: #232323
}

.screenListWrapperWeb .screenList {
    display: grid;
    grid-template-columns: minmax(calc(20% - 8px),calc(20% - 8px)) minmax(calc(20% - 8px),calc(20% - 8px)) minmax(calc(20% - 8px),calc(20% - 8px)) minmax(calc(20% - 8px),calc(20% - 8px)) minmax(calc(20% - 8px),calc(20% - 8px));
    gap: 8px
}

.screenListWrapperWeb .screenList .listItem .screenWrapper {
    position: relative;
    width: 100%;
    aspect-ratio: 1470/956;
    border-radius: 8px;
    background-color: #232323;
    outline: 1px solid #232323;
    overflow: hidden;
    cursor: zoom-in;
    transition: .2s
}

.screenListWrapperWeb .screenList .listItem .screenWrapper .screen {
    width: 100%
}

.screenListWrapperWeb .screenList .listItem .screenWrapper:has(input[type=checkbox]:checked) {
    outline: 2px solid #ec4899;
    outline-offset: 2px;
    transition: .2s
}

.screenListWrapperWeb .screenList .listItem .screenWrapper .screenHeader {
    display: none
}

@media screen and (min-width: 1024px) {
    .screenListWrapperWeb .screenList .listItem .screenWrapper .screenHeader {
        position:absolute;
        top: 0;
        left: 0;
        display: flex;
        align-items: flex-end;
        justify-content: space-between;
        width: 100%;
        padding: 12px 12px 96px;
        background: linear-gradient(0deg,transparent,rgba(0,0,0,.5) 50%,rgba(0,0,0,.95));
        pointer-events: none;
        opacity: 0
    }

    .screenListWrapperWeb .screenList .listItem .screenWrapper .screenHeader * {
        pointer-events: all
    }

    .screenListWrapperWeb .screenList .listItem .screenWrapper .screenHeader>.inner {
        display: flex;
        align-items: center;
        justify-content: flex-end;
        width: 100%
    }

    .screenListWrapperWeb .screenList .listItem .screenWrapper .screenFooter {
        position: absolute;
        bottom: 0;
        left: 0;
        display: flex;
        align-items: flex-end;
        justify-content: space-between;
        width: 100%;
        padding: 96px 12px 12px;
        background: linear-gradient(0deg,rgba(0,0,0,.95),rgba(0,0,0,.5) 50%,transparent);
        pointer-events: none;
        opacity: 0
    }
}

@media screen and (min-width: 1024px)and (min-width:1280px) {
    .screenListWrapperWeb .screenList .listItem .screenWrapper .screenFooter {
        padding:96px 16px 16px
    }
}

@media screen and (min-width: 1024px) {
    .screenListWrapperWeb .screenList .listItem .screenWrapper .screenFooter * {
        pointer-events:all
    }

    .screenListWrapperWeb .screenList .listItem .screenWrapper .screenFooter .favoriteButtonWrapper {
        display: flex;
        justify-content: flex-end;
        gap: 8px;
        width: 100%;
        pointer-events: all
    }
}

@media screen and (min-width: 1024px)and (min-width:1280px) {
    .screenListWrapperWeb .screenList .listItem .screenWrapper .screenFooter .favoriteButtonWrapper {
        gap:12px
    }
}

@media screen and (min-width: 1024px) {
    .screenListWrapperWeb .screenList .listItem .screenWrapper .screenFooter .favoriteButtonWrapper .favoriteButton {
        padding:0 9px;
        background-color: hsla(0,0%,100%,.15);
        border: 1px solid hsla(0,0%,100%,0);
        backdrop-filter: blur(16px) saturate(180%);
        -webkit-backdrop-filter: blur(25px) saturate(180%)
    }

    .screenListWrapperWeb .screenList .listItem .screenWrapper .screenFooter .favoriteButtonWrapper .favoriteButton:hover {
        background-color: hsla(0,0%,100%,.25)
    }

    .screenListWrapperWeb .screenList .listItem .screenWrapper .screenFooter .favoriteButtonWrapper .favoriteButton .buttonText {
        display: none
    }

    .screenListWrapperWeb .screenList .listItem .screenWrapper .screenFooter .favoriteButtonWrapper .dropdownButton {
        padding: 0 9px;
        background-color: hsla(0,0%,100%,.15);
        border: 1px solid hsla(0,0%,100%,0);
        backdrop-filter: blur(16px) saturate(180%);
        -webkit-backdrop-filter: blur(25px) saturate(180%)
    }

    .screenListWrapperWeb .screenList .listItem .screenWrapper .screenFooter .favoriteButtonWrapper .dropdownButton:hover {
        background-color: hsla(0,0%,100%,.25)
    }

    .screenListWrapperWeb .screenList .listItem .screenWrapper .screenFooter .favoriteButtonWrapper .dropdownButton .buttonText,.screenListWrapperWeb .screenList .listItem .screenWrapper .screenFooter .favoriteButtonWrapper .dropdownButton .proLabel {
        display: none
    }

    .screenListWrapperWeb .screenList .listItem .screenWrapper:focus .screenFooter,.screenListWrapperWeb .screenList .listItem .screenWrapper:focus .screenHeader,.screenListWrapperWeb .screenList .listItem .screenWrapper:hover .screenFooter,.screenListWrapperWeb .screenList .listItem .screenWrapper:hover .screenHeader {
        opacity: 1
    }
}

.screenListWrapperWeb .screenList .listItem .appInfo {
    display: flex;
    align-items: center;
    gap: 8px;
    width: 100%;
    pointer-events: all
}

.screenListWrapperWeb .screenList .listItem .appInfo:hover {
    cursor: pointer
}

.screenListWrapperWeb .screenList .listItem .appInfo:hover .appTitle {
    text-decoration: underline
}

.screenListWrapperWeb .screenList .listItem .appInfo .appIcon {
    width: 28px;
    height: 28px;
    border-radius: 22.5%;
    overflow: hidden;
    background-color: #232323;
    outline: 1px solid #232323
}

.screenListWrapperWeb .screenList .listItem .appInfo .appTexts {
    width: calc(100% - 36px)
}

.screenListWrapperWeb .screenList .listItem .appInfo .appTexts .appTitle {
    font-size: 14px;
    line-height: 20px;
    font-weight: 700;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis
}

.screenListWrapperWeb .screenList .listItem .screenAdBox {
    aspect-ratio: 390/844;
    padding: 16px;
    border-radius: 10%/4.7%;
    background-color: #232323
}

.flowListItem {
    background-color: #232323;
    display: flex;
    padding: 12px;
    border: 1px solid #2e2e2e;
    border-radius: 10px
}

.flowListItem .dragButton {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 24px;
    height: 32px;
    border-radius: 6px
}

.flowListItem .dragButton:hover {
    background-color: #2e2e2e;
    cursor: grab
}

.flowListItem .childrenCounter {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 24px;
    height: 32px;
    background-color: #fff;
    color: #232323;
    border-radius: 6px
}

.flowListItem .wrapper {
    width: 100%;
    display: flex;
    flex-direction: column;
    gap: 12px
}

.flowListItem .wrapper .expandContentContainer {
    display: flex;
    align-items: center;
    gap: 8px
}

.flowListItem .wrapper .expandContentContainer .expandButton {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 24px;
    height: 32px;
    border-radius: 6px
}

.flowListItem .wrapper .expandContentContainer .expandButton:hover {
    background-color: #2e2e2e;
    cursor: pointer
}

.flowListItem .wrapper .expandContentContainer .controlWrapper {
    display: flex;
    align-items: center;
    justify-content: space-between;
    width: 100%
}

.flowListItem .wrapper .expandContentContainer .controlWrapper .formContainer {
    display: flex;
    align-items: center;
    gap: 4px
}

.flowListItem .wrapper .screenListContainer {
    border-top: 1px solid #2e2e2e;
    padding-top: 12px
}

.flowListItem .wrapper .screenListContainer .screenGridListWrapperMobile {
    padding: 0
}

.flowListItem .wrapper .screenListContainer .screenGridListWrapperMobile .screenGridList {
    display: grid;
    grid-template-columns: minmax(calc(50% - 8px),calc(50% - 8px)) minmax(calc(50% - 8px),calc(50% - 8px));
    gap: 12px
}

@media screen and (min-width: 1024px) {
    .flowListItem .wrapper .screenListContainer .screenGridListWrapperMobile .screenGridList {
        grid-template-columns:minmax(calc(14.28% - 12px),calc(14.28% - 12px)) minmax(calc(14.28% - 12px),calc(14.28% - 12px)) minmax(calc(14.28% - 12px),calc(14.28% - 12px)) minmax(calc(14.28% - 12px),calc(14.28% - 12px)) minmax(calc(14.28% - 12px),calc(14.28% - 12px)) minmax(calc(14.28% - 12px),calc(14.28% - 12px)) minmax(calc(14.28% - 12px),calc(14.28% - 12px));
        gap: 12px
    }
}

@media screen and (min-width: 1536px) {
    .flowListItem .wrapper .screenListContainer .screenGridListWrapperMobile .screenGridList {
        grid-template-columns:minmax(calc(10% - 8px),calc(10% - 8px)) minmax(calc(10% - 8px),calc(10% - 8px)) minmax(calc(10% - 8px),calc(10% - 8px)) minmax(calc(10% - 8px),calc(10% - 8px)) minmax(calc(10% - 8px),calc(10% - 8px)) minmax(calc(10% - 8px),calc(10% - 8px)) minmax(calc(10% - 8px),calc(10% - 8px)) minmax(calc(10% - 8px),calc(10% - 8px)) minmax(calc(10% - 8px),calc(10% - 8px)) minmax(calc(10% - 8px),calc(10% - 8px));
        gap: 8px
    }
}

.flowListItem .wrapper .screenListContainer .screenGridListWrapperMobile .screenGridList .listItem .screenWrapper {
    position: relative;
    width: 100%;
    aspect-ratio: 390/844;
    background-color: #232323;
    outline: 1px solid #232323;
    border-radius: 8px;
    overflow: hidden;
    cursor: zoom-in;
    transition: .2s
}

.flowListItem .wrapper .screenListContainer .screenGridListWrapperMobile .screenGridList .listItem .screenWrapper .screen {
    width: 100%;
    border-radius: 8
}

.flowListItem .wrapper .screenListContainer .screenGridListWrapperMobile .screenGridList .listItem .screenWrapper:has(input[type=checkbox]:checked) {
    outline: 2px solid #ec4899;
    outline-offset: 2px;
    transition: .2s
}

.flowListItem .wrapper .screenListContainer .screenGridListWrapperMobile .screenGridList .listItem .screenWrapper .screenHeader {
    display: none
}

@media screen and (min-width: 1024px) {
    .flowListItem .wrapper .screenListContainer .screenGridListWrapperMobile .screenGridList .listItem .screenWrapper .screenHeader {
        position:absolute;
        top: 0;
        left: 0;
        display: flex;
        align-items: flex-end;
        justify-content: space-between;
        width: 100%;
        padding: 12px 12px 96px;
        background: linear-gradient(0deg,transparent,rgba(0,0,0,.5) 50%,rgba(0,0,0,.95));
        pointer-events: none;
        opacity: 0
    }

    .flowListItem .wrapper .screenListContainer .screenGridListWrapperMobile .screenGridList .listItem .screenWrapper .screenHeader * {
        pointer-events: all
    }

    .flowListItem .wrapper .screenListContainer .screenGridListWrapperMobile .screenGridList .listItem .screenWrapper .screenHeader>.inner {
        display: flex;
        align-items: center;
        justify-content: flex-end;
        width: 100%
    }

    .flowListItem .wrapper .screenListContainer .screenGridListWrapperMobile .screenGridList .listItem .screenWrapper .screenFooter {
        position: absolute;
        bottom: 0;
        left: 0;
        display: flex;
        align-items: flex-end;
        justify-content: space-between;
        width: 100%;
        padding: 96px 12px 12px;
        background: linear-gradient(0deg,rgba(0,0,0,.95),rgba(0,0,0,.5) 50%,transparent);
        pointer-events: none;
        opacity: 0
    }
}

@media screen and (min-width: 1024px)and (min-width:1280px) {
    .flowListItem .wrapper .screenListContainer .screenGridListWrapperMobile .screenGridList .listItem .screenWrapper .screenFooter {
        padding:96px 16px 16px
    }
}

@media screen and (min-width: 1024px) {
    .flowListItem .wrapper .screenListContainer .screenGridListWrapperMobile .screenGridList .listItem .screenWrapper .screenFooter * {
        pointer-events:all
    }

    .flowListItem .wrapper .screenListContainer .screenGridListWrapperMobile .screenGridList .listItem .screenWrapper .screenFooter .favoriteButtonWrapper {
        display: flex;
        justify-content: flex-end;
        gap: 8px;
        width: 100%;
        pointer-events: all
    }
}

@media screen and (min-width: 1024px)and (min-width:1280px) {
    .flowListItem .wrapper .screenListContainer .screenGridListWrapperMobile .screenGridList .listItem .screenWrapper .screenFooter .favoriteButtonWrapper {
        gap:12px
    }
}

@media screen and (min-width: 1024px) {
    .flowListItem .wrapper .screenListContainer .screenGridListWrapperMobile .screenGridList .listItem .screenWrapper .screenFooter .favoriteButtonWrapper .favoriteButton {
        padding:0 9px;
        background-color: hsla(0,0%,100%,.15);
        border: 1px solid hsla(0,0%,100%,0);
        backdrop-filter: blur(16px) saturate(180%);
        -webkit-backdrop-filter: blur(25px) saturate(180%)
    }

    .flowListItem .wrapper .screenListContainer .screenGridListWrapperMobile .screenGridList .listItem .screenWrapper .screenFooter .favoriteButtonWrapper .favoriteButton:hover {
        background-color: hsla(0,0%,100%,.25)
    }

    .flowListItem .wrapper .screenListContainer .screenGridListWrapperMobile .screenGridList .listItem .screenWrapper .screenFooter .favoriteButtonWrapper .favoriteButton .buttonText {
        display: none
    }

    .flowListItem .wrapper .screenListContainer .screenGridListWrapperMobile .screenGridList .listItem .screenWrapper .screenFooter .favoriteButtonWrapper .dropdownButton {
        padding: 0 9px;
        background-color: hsla(0,0%,100%,.15);
        border: 1px solid hsla(0,0%,100%,0);
        backdrop-filter: blur(16px) saturate(180%);
        -webkit-backdrop-filter: blur(25px) saturate(180%)
    }

    .flowListItem .wrapper .screenListContainer .screenGridListWrapperMobile .screenGridList .listItem .screenWrapper .screenFooter .favoriteButtonWrapper .dropdownButton:hover {
        background-color: hsla(0,0%,100%,.25)
    }

    .flowListItem .wrapper .screenListContainer .screenGridListWrapperMobile .screenGridList .listItem .screenWrapper .screenFooter .favoriteButtonWrapper .dropdownButton .buttonText,.flowListItem .wrapper .screenListContainer .screenGridListWrapperMobile .screenGridList .listItem .screenWrapper .screenFooter .favoriteButtonWrapper .dropdownButton .proLabel {
        display: none
    }

    .flowListItem .wrapper .screenListContainer .screenGridListWrapperMobile .screenGridList .listItem .screenWrapper:focus .screenFooter,.flowListItem .wrapper .screenListContainer .screenGridListWrapperMobile .screenGridList .listItem .screenWrapper:focus .screenHeader,.flowListItem .wrapper .screenListContainer .screenGridListWrapperMobile .screenGridList .listItem .screenWrapper:hover .screenFooter,.flowListItem .wrapper .screenListContainer .screenGridListWrapperMobile .screenGridList .listItem .screenWrapper:hover .screenHeader {
        opacity: 1
    }
}

.flowListItem .wrapper .screenListContainer .screenGridListWrapperMobile .screenGridList .listItem .appInfo {
    display: flex;
    align-items: center;
    gap: 8px;
    width: 100%;
    pointer-events: all
}

.flowListItem .wrapper .screenListContainer .screenGridListWrapperMobile .screenGridList .listItem .appInfo:hover {
    cursor: pointer
}

.flowListItem .wrapper .screenListContainer .screenGridListWrapperMobile .screenGridList .listItem .appInfo:hover .appTitle {
    text-decoration: underline
}

.flowListItem .wrapper .screenListContainer .screenGridListWrapperMobile .screenGridList .listItem .appInfo .appIcon {
    width: 28px;
    height: 28px;
    border-radius: 22.5%;
    overflow: hidden;
    background-color: #232323;
    outline: 1px solid #232323
}

.flowListItem .wrapper .screenListContainer .screenGridListWrapperMobile .screenGridList .listItem .appInfo .appTexts {
    width: calc(100% - 36px)
}

.flowListItem .wrapper .screenListContainer .screenGridListWrapperMobile .screenGridList .listItem .appInfo .appTexts .appTitle {
    font-size: 14px;
    line-height: 20px;
    font-weight: 700;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis
}

.flowListItem .wrapper .screenListContainer .screenGridListWrapperMobile .screenGridList .listItem .screenAdBox {
    aspect-ratio: 390/844;
    padding: 16px;
    border-radius: 10%/4.7%;
    background-color: #232323
}

.flowListItem .wrapper .screenListContainer .screenGridListWrapperWeb {
    padding: 16px
}

.flowListItem .wrapper .screenListContainer .screenGridListWrapperWeb .screenGridList {
    display: grid;
    grid-template-columns: 1fr;
    gap: 16px
}

@media screen and (min-width: 1024px) {
    .flowListItem .wrapper .screenListContainer .screenGridListWrapperWeb .screenGridList {
        grid-template-columns:minmax(calc(33% - 7.8px),calc(33% - 7.8px)) minmax(calc(33% - 7.8px),calc(33% - 7.8px)) minmax(calc(33% - 7.8px),calc(33% - 7.8px));
        gap: 16px
    }
}

@media screen and (min-width: 1536px) {
    .flowListItem .wrapper .screenListContainer .screenGridListWrapperWeb .screenGridList {
        grid-template-columns:minmax(calc(25% - 12px),calc(25% - 12px)) minmax(calc(25% - 12px),calc(25% - 12px)) minmax(calc(25% - 12px),calc(25% - 12px)) minmax(calc(25% - 12px),calc(25% - 12px));
        gap: 16px
    }
}

.flowListItem .wrapper .screenListContainer .screenGridListWrapperWeb .screenGridList .listItem .screenWrapper {
    position: relative;
    display: flex;
    align-items: flex-end;
    width: 100%;
    aspect-ratio: 1470/918;
    background-color: #232323;
    outline: 1px solid #232323;
    border-radius: 16px;
    overflow: hidden;
    cursor: zoom-in;
    transition: .2s
}

.flowListItem .wrapper .screenListContainer .screenGridListWrapperWeb .screenGridList .listItem .screenWrapper .screen {
    width: 100%
}

.flowListItem .wrapper .screenListContainer .screenGridListWrapperWeb .screenGridList .listItem .screenWrapper:has(input[type=checkbox]:checked) {
    outline: 2px solid #ec4899;
    outline-offset: 2px;
    transition: .2s
}

.flowListItem .wrapper .screenListContainer .screenGridListWrapperWeb .screenGridList .listItem .screenWrapper .screenHeader {
    display: none
}

@media screen and (min-width: 1024px) {
    .flowListItem .wrapper .screenListContainer .screenGridListWrapperWeb .screenGridList .listItem .screenWrapper .screenHeader {
        display:none
    }
}

@media screen and (min-width: 1024px)and (min-width:1024px) {
    .flowListItem .wrapper .screenListContainer .screenGridListWrapperWeb .screenGridList .listItem .screenWrapper .screenHeader {
        display:block;
        position: absolute;
        top: 0;
        left: 0;
        display: flex;
        align-items: flex-end;
        justify-content: space-between;
        width: 100%;
        padding: 12px 12px 24px;
        background: linear-gradient(0deg,transparent,rgba(0,0,0,.4) 50%,rgba(0,0,0,.8));
        pointer-events: none;
        opacity: 0
    }

    .flowListItem .wrapper .screenListContainer .screenGridListWrapperWeb .screenGridList .listItem .screenWrapper .screenHeader * {
        pointer-events: all
    }

    .flowListItem .wrapper .screenListContainer .screenGridListWrapperWeb .screenGridList .listItem .screenWrapper .screenHeader>.inner {
        display: flex;
        align-items: center;
        justify-content: flex-end;
        width: 100%;
        pointer-events: none
    }
}

@media screen and (min-width: 1024px) {
    .flowListItem .wrapper .screenListContainer .screenGridListWrapperWeb .screenGridList .listItem .screenWrapper .screenFooter {
        display:none;
        background: linear-gradient(0deg,rgba(0,0,0,.8),rgba(0,0,0,.4) 50%,transparent);
        pointer-events: none;
        opacity: 0
    }
}

@media screen and (min-width: 1024px)and (min-width:1024px) {
    .flowListItem .wrapper .screenListContainer .screenGridListWrapperWeb .screenGridList .listItem .screenWrapper .screenFooter {
        display:block;
        position: absolute;
        bottom: 0;
        left: 0;
        display: flex;
        align-items: flex-end;
        justify-content: space-between;
        width: 100%;
        padding: 32px 12px 12px
    }
}

@media screen and (min-width: 1024px)and (min-width:1280px) {
    .flowListItem .wrapper .screenListContainer .screenGridListWrapperWeb .screenGridList .listItem .screenWrapper .screenFooter {
        padding:96px 16px 16px
    }
}

@media screen and (min-width: 1024px) {
    .flowListItem .wrapper .screenListContainer .screenGridListWrapperWeb .screenGridList .listItem .screenWrapper .screenFooter * {
        pointer-events:all
    }

    .flowListItem .wrapper .screenListContainer .screenGridListWrapperWeb .screenGridList .listItem .screenWrapper .screenFooter .favoriteButtonWrapper {
        display: flex;
        justify-content: flex-end;
        gap: 8px;
        width: 100%;
        pointer-events: all
    }
}

@media screen and (min-width: 1024px)and (min-width:1280px) {
    .flowListItem .wrapper .screenListContainer .screenGridListWrapperWeb .screenGridList .listItem .screenWrapper .screenFooter .favoriteButtonWrapper {
        gap:12px
    }
}

@media screen and (min-width: 1024px) {
    .flowListItem .wrapper .screenListContainer .screenGridListWrapperWeb .screenGridList .listItem .screenWrapper .screenFooter .favoriteButtonWrapper .favoriteButton {
        padding:0 9px;
        background-color: hsla(0,0%,100%,.15);
        border: 1px solid hsla(0,0%,100%,0);
        backdrop-filter: blur(16px) saturate(180%);
        -webkit-backdrop-filter: blur(25px) saturate(180%)
    }

    .flowListItem .wrapper .screenListContainer .screenGridListWrapperWeb .screenGridList .listItem .screenWrapper .screenFooter .favoriteButtonWrapper .favoriteButton:hover {
        background-color: hsla(0,0%,100%,.25)
    }

    .flowListItem .wrapper .screenListContainer .screenGridListWrapperWeb .screenGridList .listItem .screenWrapper .screenFooter .favoriteButtonWrapper .favoriteButton .buttonText {
        display: none
    }

    .flowListItem .wrapper .screenListContainer .screenGridListWrapperWeb .screenGridList .listItem .screenWrapper .screenFooter .favoriteButtonWrapper .dropdownButton {
        padding: 0 9px;
        background-color: hsla(0,0%,100%,.15);
        border: 1px solid hsla(0,0%,100%,0);
        backdrop-filter: blur(16px) saturate(180%);
        -webkit-backdrop-filter: blur(25px) saturate(180%)
    }

    .flowListItem .wrapper .screenListContainer .screenGridListWrapperWeb .screenGridList .listItem .screenWrapper .screenFooter .favoriteButtonWrapper .dropdownButton:hover {
        background-color: hsla(0,0%,100%,.25)
    }

    .flowListItem .wrapper .screenListContainer .screenGridListWrapperWeb .screenGridList .listItem .screenWrapper .screenFooter .favoriteButtonWrapper .dropdownButton .buttonText,.flowListItem .wrapper .screenListContainer .screenGridListWrapperWeb .screenGridList .listItem .screenWrapper .screenFooter .favoriteButtonWrapper .dropdownButton .proLabel {
        display: none
    }

    .flowListItem .wrapper .screenListContainer .screenGridListWrapperWeb .screenGridList .listItem .screenWrapper:focus .screenFooter,.flowListItem .wrapper .screenListContainer .screenGridListWrapperWeb .screenGridList .listItem .screenWrapper:focus .screenHeader,.flowListItem .wrapper .screenListContainer .screenGridListWrapperWeb .screenGridList .listItem .screenWrapper:hover .screenFooter,.flowListItem .wrapper .screenListContainer .screenGridListWrapperWeb .screenGridList .listItem .screenWrapper:hover .screenHeader {
        opacity: 1
    }
}

.flowListItem .wrapper .screenListContainer .screenGridListWrapperWeb .screenGridList .listItem .appInfo {
    display: flex;
    align-items: center;
    gap: 8px;
    width: 100%;
    pointer-events: all
}

.flowListItem .wrapper .screenListContainer .screenGridListWrapperWeb .screenGridList .listItem .appInfo:hover {
    cursor: pointer
}

.flowListItem .wrapper .screenListContainer .screenGridListWrapperWeb .screenGridList .listItem .appInfo:hover .appTitle {
    text-decoration: underline
}

.flowListItem .wrapper .screenListContainer .screenGridListWrapperWeb .screenGridList .listItem .appInfo .appIcon {
    width: 28px;
    height: 28px;
    border-radius: 22.5%;
    overflow: hidden;
    background-color: #232323;
    outline: 1px solid #232323
}

.flowListItem .wrapper .screenListContainer .screenGridListWrapperWeb .screenGridList .listItem .appInfo .appTexts {
    width: calc(100% - 36px)
}

.flowListItem .wrapper .screenListContainer .screenGridListWrapperWeb .screenGridList .listItem .appInfo .appTexts .appTitle {
    font-size: 14px;
    line-height: 20px;
    font-weight: 700;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis
}

.flowListItem .wrapper .screenListContainer .screenGridListWrapperWeb .screenGridList .listItem .screenAdBox {
    aspect-ratio: 390/844;
    padding: 16px;
    border-radius: 10%/4.7%;
    background-color: #232323
}

.clonedItem {
    position: absolute;
    left: 0;
    top: 0;
    transition: .2s;
    background: transparent;
    border-radius: 10px
}

.screenFlowConnectEditor {
    display: grid;
    grid-template-columns: 1fr 240px;
    gap: 8px
}

.screenFlowConnectEditor .screenListWrapper {
    height: calc(100svh - 80px);
    padding: 8px;
    border: 1px solid #2e2e2e;
    border-radius: 20px;
    overflow: scroll
}

.screenFlowConnectEditor .screenListWrapper .toolbar {
    position: fixed;
    bottom: 16px;
    left: 80px;
    width: 400px;
    padding: 12px;
    background-color: rgba(46,46,46,.5);
    border: 1px solid hsla(0,0%,100%,.05);
    backdrop-filter: blur(40px);
    -webkit-backdrop-filter: blur(40px);
    border-radius: 32px
}

.screenFlowConnectEditor .screenListWrapper .toolbar .thumbnailList {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 4px
}

.screenFlowConnectEditor .screenListWrapper .toolbar .thumbnailList .listItem {
    border-radius: 20px;
    overflow: hidden
}

.screenFlowConnectEditor .screenListWrapper .toolbar .leftSection {
    display: flex;
    align-items: center;
    justify-content: space-between
}

.screenFlowConnectEditor .flowSelectionSidebar {
    position: sticky;
    top: 16px;
    right: 0;
    padding: 8px;
    width: 100%;
    height: calc(100svh - 80px);
    overflow: scroll;
    border: 1px solid #2e2e2e;
    border-radius: 20px
}

.screenFlowConnectEditor .flowSelectionSidebar .parent:not(:first-child) {
    border-top: 1px solid #2e2e2e;
    margin-top: 8px;
    padding-top: 8px
}

.screenFlowConnectEditor .flowSelectionSidebar .firstChild {
    position: relative;
    padding-left: 20px
}

.screenFlowConnectEditor .flowSelectionSidebar .firstChild:before {
    content: "";
    position: absolute;
    left: 8px;
    top: 16px;
    width: 12px;
    height: 1px;
    background-color: #2e2e2e
}

.screenFlowConnectEditor .flowSelectionSidebar .secondChild {
    position: relative;
    padding-left: 40px
}

.screenFlowConnectEditor .flowSelectionSidebar .secondChild:before {
    content: "";
    position: absolute;
    left: 8px;
    top: 16px;
    width: 32px;
    height: 1px;
    background-color: #2e2e2e
}

.screenFlowConnectEditor .flowSelectionSidebar .thirdChild {
    position: relative;
    padding-left: 60px
}

.screenFlowConnectEditor .flowSelectionSidebar .thirdChild:before {
    content: "";
    position: absolute;
    left: 8px;
    top: 16px;
    width: 52px;
    height: 1px;
    background-color: #2e2e2e
}

.screenFlowConnectEditor .flowSelectionSidebar .floatButton {
    position: sticky;
    bottom: 0;
    left: 0
}

.fileInputBar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    border: 1px solid #2e2e2e;
    padding: 8px;
    border-radius: 20px
}

.adminScreenDetailSheet {
    display: grid;
    grid-template-columns: 40% 1fr
}

.adminScreenDetailSheet .screenWrapper {
    display: flex;
    align-items: center;
    justify-content: center;
    height: 100vh;
    padding: 12px
}

.adminScreenDetailSheet .screenWrapper .screenImageContainer {
    position: relative;
    max-height: 90vh;
    width: auto;
    max-width: 100%
}

.adminScreenDetailSheet .screenWrapper .screenImageContainer .profileImage {
    width: 100%;
    height: 100%;
    border: 1px solid #2e2e2e;
    border-radius: 50px;
    -o-object-fit: cover;
    object-fit: cover
}

.adminScreenDetailSheet .screenWrapper .screenImageContainer .iconBox {
    position: absolute;
    bottom: 0;
    right: -16px;
    display: flex;
    align-items: center;
    justify-content: center;
    width: 32px;
    height: 32px;
    border-radius: 50px;
    background-color: #2e2e2e;
    box-shadow: 0 2px 8px rgba(0,0,0,.1)
}

.adminScreenDetailSheet .screenWrapper .screenImageContainer .profileIcon {
    font-size: 72px;
    color: #161616
}

.adminScreenDetailSheet .screenWrapper .screen {
    max-height: 90vh;
    width: auto;
    max-width: 100%
}

.adminScreenDetailSheet .conponentListWrapper {
    flex-grow: 1;
    border-left: 1px solid #2e2e2e
}

.adminScreenDetailSheet .conponentListWrapper .componentsParentWrapper {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr 1fr
}

.adminScreenDetailSheet .conponentListWrapper .componentsParentWrapper .categoryList .listItem {
    margin-bottom: -4px
}

*,:after,:before {
    --tw-border-spacing-x: 0;
    --tw-border-spacing-y: 0;
    --tw-translate-x: 0;
    --tw-translate-y: 0;
    --tw-rotate: 0;
    --tw-skew-x: 0;
    --tw-skew-y: 0;
    --tw-scale-x: 1;
    --tw-scale-y: 1;
    --tw-pan-x: ;
    --tw-pan-y: ;
    --tw-pinch-zoom: ;
    --tw-scroll-snap-strictness: proximity;
    --tw-gradient-from-position: ;
    --tw-gradient-via-position: ;
    --tw-gradient-to-position: ;
    --tw-ordinal: ;
    --tw-slashed-zero: ;
    --tw-numeric-figure: ;
    --tw-numeric-spacing: ;
    --tw-numeric-fraction: ;
    --tw-ring-inset: ;
    --tw-ring-offset-width: 0px;
    --tw-ring-offset-color: #fff;
    --tw-ring-color: rgba(59,130,246,.5);
    --tw-ring-offset-shadow: 0 0 #0000;
    --tw-ring-shadow: 0 0 #0000;
    --tw-shadow: 0 0 #0000;
    --tw-shadow-colored: 0 0 #0000;
    --tw-blur: ;
    --tw-brightness: ;
    --tw-contrast: ;
    --tw-grayscale: ;
    --tw-hue-rotate: ;
    --tw-invert: ;
    --tw-saturate: ;
    --tw-sepia: ;
    --tw-drop-shadow: ;
    --tw-backdrop-blur: ;
    --tw-backdrop-brightness: ;
    --tw-backdrop-contrast: ;
    --tw-backdrop-grayscale: ;
    --tw-backdrop-hue-rotate: ;
    --tw-backdrop-invert: ;
    --tw-backdrop-opacity: ;
    --tw-backdrop-saturate: ;
    --tw-backdrop-sepia: ;
    --tw-contain-size: ;
    --tw-contain-layout: ;
    --tw-contain-paint: ;
    --tw-contain-style:
}

::backdrop {
    --tw-border-spacing-x: 0;
    --tw-border-spacing-y: 0;
    --tw-translate-x: 0;
    --tw-translate-y: 0;
    --tw-rotate: 0;
    --tw-skew-x: 0;
    --tw-skew-y: 0;
    --tw-scale-x: 1;
    --tw-scale-y: 1;
    --tw-pan-x: ;
    --tw-pan-y: ;
    --tw-pinch-zoom: ;
    --tw-scroll-snap-strictness: proximity;
    --tw-gradient-from-position: ;
    --tw-gradient-via-position: ;
    --tw-gradient-to-position: ;
    --tw-ordinal: ;
    --tw-slashed-zero: ;
    --tw-numeric-figure: ;
    --tw-numeric-spacing: ;
    --tw-numeric-fraction: ;
    --tw-ring-inset: ;
    --tw-ring-offset-width: 0px;
    --tw-ring-offset-color: #fff;
    --tw-ring-color: rgba(59,130,246,.5);
    --tw-ring-offset-shadow: 0 0 #0000;
    --tw-ring-shadow: 0 0 #0000;
    --tw-shadow: 0 0 #0000;
    --tw-shadow-colored: 0 0 #0000;
    --tw-blur: ;
    --tw-brightness: ;
    --tw-contrast: ;
    --tw-grayscale: ;
    --tw-hue-rotate: ;
    --tw-invert: ;
    --tw-saturate: ;
    --tw-sepia: ;
    --tw-drop-shadow: ;
    --tw-backdrop-blur: ;
    --tw-backdrop-brightness: ;
    --tw-backdrop-contrast: ;
    --tw-backdrop-grayscale: ;
    --tw-backdrop-hue-rotate: ;
    --tw-backdrop-invert: ;
    --tw-backdrop-opacity: ;
    --tw-backdrop-saturate: ;
    --tw-backdrop-sepia: ;
    --tw-contain-size: ;
    --tw-contain-layout: ;
    --tw-contain-paint: ;
    --tw-contain-style:
}

/*
! tailwindcss v3.4.15 | MIT License | https://tailwindcss.com
*/
*,:after,:before {
    box-sizing: border-box;
    border: 0 solid #e5e7eb
}

:after,:before {
    --tw-content: ""
}

:host,html {
    line-height: 1.5;
    -webkit-text-size-adjust: 100%;
    -moz-tab-size: 4;
    -o-tab-size: 4;
    tab-size: 4;
    font-family: ui-sans-serif,system-ui,sans-serif,Apple Color Emoji,Segoe UI Emoji,Segoe UI Symbol,Noto Color Emoji;
    font-feature-settings: normal;
    font-variation-settings: normal;
    -webkit-tap-highlight-color: transparent
}

body {
    margin: 0;
    line-height: inherit
}

hr {
    height: 0;
    color: inherit;
    border-top-width: 1px
}

abbr:where([title]) {
    -webkit-text-decoration: underline dotted;
    text-decoration: underline dotted
}

h1,h2,h3,h4,h5,h6 {
    font-size: inherit;
    font-weight: inherit
}

a {
    color: inherit;
    text-decoration: inherit
}

b,strong {
    font-weight: bolder
}

code,kbd,pre,samp {
    font-family: ui-monospace,SFMono-Regular,Menlo,Monaco,Consolas,Liberation Mono,Courier New,monospace;
    font-feature-settings: normal;
    font-variation-settings: normal;
    font-size: 1em
}

small {
    font-size: 80%
}

sub,sup {
    font-size: 75%;
    line-height: 0;
    position: relative;
    vertical-align: baseline
}

sub {
    bottom: -.25em
}

sup {
    top: -.5em
}

table {
    text-indent: 0;
    border-color: inherit;
    border-collapse: collapse
}

button,input,optgroup,select,textarea {
    font-family: inherit;
    font-feature-settings: inherit;
    font-variation-settings: inherit;
    font-size: 100%;
    font-weight: inherit;
    line-height: inherit;
    letter-spacing: inherit;
    color: inherit;
    margin: 0;
    padding: 0
}

button,select {
    text-transform: none
}

button,input:where([type=button]),input:where([type=reset]),input:where([type=submit]) {
    -webkit-appearance: button;
    background-color: transparent;
    background-image: none
}

:-moz-focusring {
    outline: auto
}

:-moz-ui-invalid {
    box-shadow: none
}

progress {
    vertical-align: baseline
}

::-webkit-inner-spin-button,::-webkit-outer-spin-button {
    height: auto
}

[type=search] {
    -webkit-appearance: textfield;
    outline-offset: -2px
}

::-webkit-search-decoration {
    -webkit-appearance: none
}

::-webkit-file-upload-button {
    -webkit-appearance: button;
    font: inherit
}

summary {
    display: list-item
}

blockquote,dd,dl,figure,h1,h2,h3,h4,h5,h6,hr,p,pre {
    margin: 0
}

fieldset {
    margin: 0
}

fieldset,legend {
    padding: 0
}

menu,ol,ul {
    list-style: none;
    margin: 0;
    padding: 0
}

dialog {
    padding: 0
}

textarea {
    resize: vertical
}

input::-moz-placeholder,textarea::-moz-placeholder {
    opacity: 1;
    color: #9ca3af
}

input::placeholder,textarea::placeholder {
    opacity: 1;
    color: #9ca3af
}

[role=button],button {
    cursor: pointer
}

:disabled {
    cursor: default
}

audio,canvas,embed,iframe,img,object,svg,video {
    display: block;
    vertical-align: middle
}

img,video {
    max-width: 100%;
    height: auto
}

[hidden]:where(:not([hidden=until-found])) {
    display: none
}

.pointer-events-none {
    pointer-events: none
}

.absolute {
    position: absolute
}

.relative {
    position: relative
}

.z-10 {
    z-index: 10
}

.m-4 {
    margin: 1rem
}

.mx-4 {
    margin-left: 1rem;
    margin-right: 1rem
}

.mx-auto {
    margin-left: auto;
    margin-right: auto
}

.my-16 {
    margin-top: 4rem;
    margin-bottom: 4rem
}

.my-2 {
    margin-top: .5rem;
    margin-bottom: .5rem
}

.my-4 {
    margin-top: 1rem;
    margin-bottom: 1rem
}

.mb-1 {
    margin-bottom: .25rem
}

.mb-12 {
    margin-bottom: 3rem
}

.mb-16 {
    margin-bottom: 4rem
}

.mb-2 {
    margin-bottom: .5rem
}

.mb-3 {
    margin-bottom: .75rem
}

.mb-4 {
    margin-bottom: 1rem
}

.mb-6 {
    margin-bottom: 1.5rem
}

.mb-8 {
    margin-bottom: 2rem
}

.ml-1 {
    margin-left: .25rem
}

.ml-2 {
    margin-left: .5rem
}

.ml-4 {
    margin-left: 1rem
}

.ml-auto {
    margin-left: auto
}

.mr-4 {
    margin-right: 1rem
}

.mt-0\.5 {
    margin-top: .125rem
}

.mt-1 {
    margin-top: .25rem
}

.mt-12 {
    margin-top: 3rem
}

.mt-16 {
    margin-top: 4rem
}

.mt-2 {
    margin-top: .5rem
}

.mt-3 {
    margin-top: .75rem
}

.mt-4 {
    margin-top: 1rem
}

.mt-6 {
    margin-top: 1.5rem
}

.mt-8 {
    margin-top: 2rem
}

.block {
    display: block
}

.inline {
    display: inline
}

.flex {
    display: flex
}

.table {
    display: table
}

.list-item {
    display: list-item
}

.hidden {
    display: none
}

.w-10 {
    width: 2.5rem
}

.w-56 {
    width: 14rem
}

.w-8 {
    width: 2rem
}

.w-full {
    width: 100%
}

.w-max {
    width: -moz-max-content;
    width: max-content
}

.-translate-y-4 {
    --tw-translate-y: -1rem
}

.-translate-y-4,.-translate-y-8 {
    transform: translate(var(--tw-translate-x),var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y))
}

.-translate-y-8 {
    --tw-translate-y: -2rem
}

.translate-x-0 {
    --tw-translate-x: 0px
}

.translate-x-0,.translate-x-1\/3 {
    transform: translate(var(--tw-translate-x),var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y))
}

.translate-x-1\/3 {
    --tw-translate-x: 33.333333%
}

.translate-y-0 {
    --tw-translate-y: 0px
}

.translate-y-0,.translate-y-8 {
    transform: translate(var(--tw-translate-x),var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y))
}

.translate-y-8 {
    --tw-translate-y: 2rem
}

.translate-y-full {
    --tw-translate-y: 100%
}

.transform,.translate-y-full {
    transform: translate(var(--tw-translate-x),var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y))
}

.resize {
    resize: both
}

.list-none {
    list-style-type: none
}

.flex-col {
    flex-direction: column
}

.items-center {
    align-items: center
}

.justify-end {
    justify-content: flex-end
}

.justify-between {
    justify-content: space-between
}

.gap-1 {
    gap: .25rem
}

.gap-2 {
    gap: .5rem
}

.gap-4 {
    gap: 1rem
}

.rounded-md {
    border-radius: .375rem
}

.rounded-xl {
    border-radius: .75rem
}

.border {
    border-width: 1px
}

.border-t {
    border-top-width: 1px
}

.bg-neutral-800 {
    --tw-bg-opacity: 1;
    background-color: rgb(38 38 38/var(--tw-bg-opacity,1))
}

.bg-white\/5 {
    background-color: hsla(0,0%,100%,.05)
}

.p-2 {
    padding: .5rem
}

.p-3 {
    padding: .75rem
}

.p-4 {
    padding: 1rem
}

.p-6 {
    padding: 1.5rem
}

.p-8 {
    padding: 2rem
}

.px-2 {
    padding-left: .5rem;
    padding-right: .5rem
}

.px-4 {
    padding-left: 1rem;
    padding-right: 1rem
}

.py-1 {
    padding-top: .25rem;
    padding-bottom: .25rem
}

.py-16 {
    padding-top: 4rem;
    padding-bottom: 4rem
}

.py-4 {
    padding-top: 1rem;
    padding-bottom: 1rem
}

.py-8 {
    padding-top: 2rem;
    padding-bottom: 2rem
}

.pb-0 {
    padding-bottom: 0
}

.pb-16 {
    padding-bottom: 4rem
}

.pb-24 {
    padding-bottom: 6rem
}

.pb-32 {
    padding-bottom: 8rem
}

.pb-4 {
    padding-bottom: 1rem
}

.pb-8 {
    padding-bottom: 2rem
}

.pl-12 {
    padding-left: 3rem
}

.pl-2 {
    padding-left: .5rem
}

.pt-0 {
    padding-top: 0
}

.pt-12 {
    padding-top: 3rem
}

.pt-16 {
    padding-top: 4rem
}

.pt-2 {
    padding-top: .5rem
}

.pt-4 {
    padding-top: 1rem
}

.pt-8 {
    padding-top: 2rem
}

.text-center {
    text-align: center
}

.align-middle {
    vertical-align: middle
}

.text-base {
    font-size: 1rem;
    line-height: 1.5rem
}

.text-lg {
    font-size: 1.125rem;
    line-height: 1.75rem
}

.text-sm {
    font-size: .875rem;
    line-height: 1.25rem
}

.text-xs {
    font-size: .75rem;
    line-height: 1rem
}

.font-semibold {
    font-weight: 600
}

.capitalize {
    text-transform: capitalize
}

.italic {
    font-style: italic
}

.opacity-0 {
    opacity: 0
}

.opacity-100 {
    opacity: 1
}

.opacity-25 {
    opacity: .25
}

.opacity-70 {
    opacity: .7
}

.filter {
    filter: var(--tw-blur) var(--tw-brightness) var(--tw-contrast) var(--tw-grayscale) var(--tw-hue-rotate) var(--tw-invert) var(--tw-saturate) var(--tw-sepia) var(--tw-drop-shadow)
}

.transition {
    transition-property: color,background-color,border-color,text-decoration-color,fill,stroke,opacity,box-shadow,transform,filter,-webkit-backdrop-filter;
    transition-property: color,background-color,border-color,text-decoration-color,fill,stroke,opacity,box-shadow,transform,filter,backdrop-filter;
    transition-property: color,background-color,border-color,text-decoration-color,fill,stroke,opacity,box-shadow,transform,filter,backdrop-filter,-webkit-backdrop-filter;
    transition-timing-function: cubic-bezier(.4,0,.2,1);
    transition-duration: .15s
}

.transition-opacity {
    transition-property: opacity;
    transition-timing-function: cubic-bezier(.4,0,.2,1);
    transition-duration: .15s
}

.duration-200 {
    transition-duration: .2s
}

.duration-300 {
    transition-duration: .3s
}

.ease-in {
    transition-timing-function: cubic-bezier(.4,0,1,1)
}

.ease-in-out {
    transition-timing-function: cubic-bezier(.4,0,.2,1)
}

.ease-out {
    transition-timing-function: cubic-bezier(0,0,.2,1)
}

body>*,html {
    color: #fff
}

@media (min-width: 1024px) {
    .lg\:block {
        display:block
    }

    .lg\:hidden {
        display: none
    }

    .lg\:translate-y-16 {
        --tw-translate-y: 4rem;
        transform: translate(var(--tw-translate-x),var(--tw-translate-y)) rotate(var(--tw-rotate)) skewX(var(--tw-skew-x)) skewY(var(--tw-skew-y)) scaleX(var(--tw-scale-x)) scaleY(var(--tw-scale-y))
    }
}

.Dropdown_textGray200__8Duqu {
    color: #d4d4d4
}

.Dropdown_borderGray900__XkmFM {
    border-color: #2e2e2e
}

.Dropdown_dropdownButtonMd__9Fqun {
    display: flex;
    align-items: center;
    justify-content: center;
    height: 40px;
    width: 40px;
    background-color: rgba(50,50,50,.5);
    border: 1px solid hsla(0,0%,100%,.1);
    backdrop-filter: blur(40px);
    -webkit-backdrop-filter: blur(40px);
    border-radius: 100px;
    transition: .2s
}

.Dropdown_dropdownButtonMd__9Fqun:active {
    transform: scale(.96)
}

.Dropdown_dropdownButtonMd__9Fqun:hover {
    background-color: rgba(75,75,75,.5);
    transition: .2s
}

.Dropdown_dropdownButtonMd__9Fqun:disabled:hover,.Dropdown_dropdownButtonSm__I6gSs {
    background-color: rgba(50,50,50,.5)
}

.Dropdown_dropdownButtonSm__I6gSs {
    display: flex;
    align-items: center;
    justify-content: center;
    height: 32px;
    width: 32px;
    border: 1px solid hsla(0,0%,100%,.1);
    backdrop-filter: blur(40px);
    -webkit-backdrop-filter: blur(40px);
    border-radius: 100px;
    transition: .2s
}

.Dropdown_dropdownButtonSm__I6gSs:active {
    transform: scale(.96)
}

.Dropdown_dropdownButtonSm__I6gSs:hover {
    background-color: rgba(75,75,75,.5);
    transition: .2s
}

.Dropdown_dropdownButtonSm__I6gSs:disabled:hover {
    background-color: rgba(50,50,50,.5)
}

.Dropdown_dropdownMenuWrapper__wjWX4 {
    position: relative;
    width: 272px;
    max-height: 360px;
    padding: 8px;
    background-color: rgba(46,46,46,.8);
    border: 1px solid hsla(0,0%,100%,.05);
    backdrop-filter: blur(40px);
    -webkit-backdrop-filter: blur(40px);
    border-radius: 12px;
    box-shadow: 0 4px 24px rgba(0,0,0,.25);
    z-index: 9999;
    overflow: scroll
}

.Dropdown_dropdownMenuWrapper__wjWX4:focus,.Dropdown_dropdownMenuWrapper__wjWX4:focus-visible {
    outline: 1px solid #fff
}

.Dropdown_dropdownMenuWrapper__wjWX4 .Dropdown_menuList__mRYzq {
    display: flex;
    align-items: center;
    gap: 8px;
    padding: 10px
}

.Dropdown_dropdownMenuWrapper__wjWX4 .Dropdown_menuList__mRYzq .Dropdown_avatarButton__z_Hbx {
    width: 32px;
    height: 32px;
    border-radius: 50px;
    border: 1px solid hsla(0,0%,100%,.05);
    overflow: hidden
}

.Dropdown_dropdownMenuWrapper__wjWX4 .Dropdown_menuList__mRYzq .Dropdown_userName__QIblL {
    font-size: 16px;
    line-height: 24px;
    font-weight: 700
}

.Dropdown_dropdownMenuWrapper__wjWX4 .Dropdown_menuButton__zXRij {
    display: flex;
    align-items: center;
    gap: 8px;
    width: 100%;
    padding: 10px;
    border-radius: 8px;
    transition: all .2s
}

.Dropdown_dropdownMenuWrapper__wjWX4 .Dropdown_menuButton__zXRij .Dropdown_buttonText__3mK7b {
    font-size: 14px;
    line-height: 20px
}

.Dropdown_dropdownMenuWrapper__wjWX4 .Dropdown_menuButton__zXRij:hover {
    border-radius: 8px;
    background-color: hsla(0,0%,100%,.1);
    transition: all .2s;
    outline: none
}

.Dropdown_dropdownMenuWrapper__wjWX4 .Dropdown_menuButton__zXRij:focus {
    outline: none
}

.Dropdown_dropdownMenuWrapper__wjWX4 .Dropdown_menuButton__zXRij:disabled {
    opacity: .5;
    cursor: not-allowed
}

.Dropdown_dropdownMenuWrapper__wjWX4 .Dropdown_menuButtonDanger__grxcq {
    display: flex;
    align-items: center;
    gap: 8px;
    width: 100%;
    padding: 10px;
    border-radius: 8px;
    transition: all .2s
}

.Dropdown_dropdownMenuWrapper__wjWX4 .Dropdown_menuButtonDanger__grxcq .Dropdown_icon__MqXI5 {
    color: #ef4444
}

.Dropdown_dropdownMenuWrapper__wjWX4 .Dropdown_menuButtonDanger__grxcq .Dropdown_buttonText__3mK7b {
    font-size: 14px;
    line-height: 20px;
    color: #ef4444
}

.Dropdown_dropdownMenuWrapper__wjWX4 .Dropdown_menuButtonDanger__grxcq:hover {
    border-radius: 8px;
    background-color: rgba(239,68,68,.2);
    transition: all .2s;
    outline: none
}

.Dropdown_dropdownMenuWrapper__wjWX4 .Dropdown_menuButtonDanger__grxcq:focus {
    outline: none
}

.Dropdown_dropdownMenuWrapper__wjWX4 .Dropdown_menuButtonDanger__grxcq:disabled {
    opacity: .5;
    cursor: not-allowed
}

.Dropdown_separator__qyswG {
    width: 100%;
    border-top: 1px solid hsla(0,0%,100%,.1)
}

.Dropdown_dropdownMenuWrapper__wjWX4 {
    animation-duration: .3s;
    animation-timing-function: cubic-bezier(.16,1,.3,1)
}

.Dropdown_dropdownMenuWrapper__wjWX4[data-side=top] {
    animation-name: Dropdown_slideUp__SMJyc
}

.Dropdown_dropdownMenuWrapper__wjWX4[data-side=bottom] {
    animation-name: Dropdown_slideDown__0sV1l
}

@keyframes Dropdown_slideUp__SMJyc {
    0% {
        opacity: 0;
        transform: translateY(10px)
    }

    to {
        opacity: 1;
        transform: translateY(0)
    }
}

@keyframes Dropdown_slideDown__0sV1l {
    0% {
        opacity: 0;
        transform: translateY(-10px)
    }

    to {
        opacity: 1;
        transform: translateY(0)
    }
}

.Dropdown_TooltipWrapper__RdZgW {
    background-color: red
}

.Dropdown_TooltipContent__92ggi {
    background-color: rgba(46,46,46,.8);
    border: 1px solid hsla(0,0%,100%,.05);
    backdrop-filter: blur(40px);
    -webkit-backdrop-filter: blur(40px);
    box-shadow: 0 0 8px rgba(0,0,0,.5);
    padding: 4px 8px;
    font-size: 14px;
    line-height: 20px;
    border-radius: 8px;
    z-index: 999999
}

.Dropdown_dropdpwnButtonForWorkspace__YXRpN {
    display: flex;
    align-items: center;
    gap: 8px;
    padding: 6px;
    border-radius: 8px;
    transition: all .2s
}

.Dropdown_dropdpwnButtonForWorkspace__YXRpN:hover {
    background-color: #232323;
    transition: all .2s
}

.Dropdown_profileBox__qS9a3 {
    display: flex;
    align-items: center;
    gap: 8px
}

.Dropdown_profileBox__qS9a3 .Dropdown_avatar__fJQZT {
    width: 24px;
    height: 24px;
    border: 1px solid #2e2e2e;
    border-radius: 4px;
    overflow: hidden
}

.Dropdown_profileBox__qS9a3 .Dropdown_avatarFallback__gx4o3 {
    width: 24px;
    height: 24px;
    border-radius: 4px;
    background-color: #707070;
    color: #161616;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 700;
    font-size: 14px;
    line-height: 20px
}

.Dropdown_profileBox__qS9a3 .Dropdown_name__vXXRd {
    font-size: 14px;
    line-height: 20px;
    font-weight: 700;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap
}

.Dropdown_profileBox__qS9a3 .Dropdown_label__Be0Z1 {
    font-size: 12px;
    line-height: 16px;
    padding: 2px 8px;
    border-radius: 50px
}

.Dropdown_profileBox__qS9a3 .Dropdown_colorFree__PM2NE {
    background-color: #2e2e2e
}

.Dropdown_profileBox__qS9a3 .Dropdown_colorPro__yzIHd {
    background-color: rgba(236,72,153,.25);
    color: #f9a8d4
}

.Dropdown_profileBox__qS9a3 .Dropdown_colorTeam__ARK0m {
    background-color: rgba(37,99,235,.25);
    color: #93c5fd
}

.Dropdown_dorpdownIcon__A_jbG {
    color: #a0a0a0;
    margin-right: 4px
}

.SearchBar_textGray200__2lsdy {
    color: #d4d4d4
}

.SearchBar_borderGray900__9ZTXH {
    border-color: #2e2e2e
}

.SearchBar_modalBackground__NFWTD {
    position: fixed;
    inset: 0;
    margin: auto;
    background-color: rgba(0,0,0,.75);
    z-index: 8999
}

.SearchBar_dialog__UYRLM {
    position: fixed;
    inset: 0;
    margin: auto;
    z-index: 9000;
    pointer-events: none
}

.SearchBar_dialog__UYRLM .SearchBar_card__UKy0n {
    position: fixed;
    inset: 0;
    margin: 32px auto auto;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    width: calc(100% - 32px);
    height: -moz-max-content;
    height: max-content;
    background-color: #232323;
    border: 1px solid #2e2e2e;
    border-radius: 16px;
    pointer-events: all;
    overflow: scroll
}

@media screen and (min-width: 1024px) {
    .SearchBar_dialog__UYRLM .SearchBar_card__UKy0n {
        width:640px
    }
}

.SearchBar_dialog__UYRLM .SearchBar_card__UKy0n .SearchBar_cardInner__Hx4Cq {
    position: relative;
    width: 100%
}

.SearchBar_dialog__UYRLM .SearchBar_card__UKy0n .SearchBar_cardInner__Hx4Cq .SearchBar_searchIcon__in2yd {
    position: absolute;
    top: 18px;
    left: 16px;
    z-index: 99
}

.SearchBar_dialog__UYRLM .SearchBar_card__UKy0n .SearchBar_cardInner__Hx4Cq .SearchBar_textInput__QGSqz {
    position: sticky;
    top: 0;
    left: 0;
    width: 100%;
    padding: 16px 16px 16px 52px;
    background-color: #232323
}

.SearchBar_dialog__UYRLM .SearchBar_card__UKy0n .SearchBar_cardInner__Hx4Cq .SearchBar_textInput__QGSqz::-moz-placeholder {
    color: #a0a0a0
}

.SearchBar_dialog__UYRLM .SearchBar_card__UKy0n .SearchBar_cardInner__Hx4Cq .SearchBar_textInput__QGSqz::placeholder {
    color: #a0a0a0
}

.SearchBar_dialog__UYRLM .SearchBar_card__UKy0n .SearchBar_cardInner__Hx4Cq .SearchBar_suggestionContainer__doJGu {
    height: -moz-max-content;
    height: max-content;
    max-height: 480px;
    padding: 8px;
    border-top: 1px solid #2e2e2e;
    overflow: scroll
}

.SearchBar_dialog__UYRLM .SearchBar_card__UKy0n .SearchBar_cardInner__Hx4Cq .SearchBar_suggestionContainer__doJGu .SearchBar_section__4j5My .SearchBar_sectionTitle__hotur {
    padding: 8px;
    font-size: 12px;
    line-height: 16px;
    font-weight: 700;
    color: #a0a0a0
}

.SearchBar_dialog__UYRLM .SearchBar_card__UKy0n .SearchBar_cardInner__Hx4Cq .SearchBar_suggestionContainer__doJGu .SearchBar_appList__AOCli {
    width: 100%
}

.SearchBar_dialog__UYRLM .SearchBar_card__UKy0n .SearchBar_cardInner__Hx4Cq .SearchBar_suggestionContainer__doJGu .SearchBar_listItemInner__eqFOY {
    display: flex;
    align-items: center;
    gap: 8px;
    width: 100%;
    padding: 8px
}

.SearchBar_dialog__UYRLM .SearchBar_card__UKy0n .SearchBar_cardInner__Hx4Cq .SearchBar_suggestionContainer__doJGu .SearchBar_listItemInner__eqFOY .SearchBar_iconBox__01P_O {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 32px;
    height: 32px;
    border-radius: 20%;
    background-color: #3e3e3e
}

.SearchBar_dialog__UYRLM .SearchBar_card__UKy0n .SearchBar_cardInner__Hx4Cq .SearchBar_suggestionContainer__doJGu .SearchBar_listItemInner__eqFOY .SearchBar_appIcon__FqIbD {
    width: 32px;
    height: 32px;
    -o-object-fit: cover;
    object-fit: cover;
    border: 1px solid #2e2e2e;
    border-radius: 20%
}

.SearchBar_dialog__UYRLM .SearchBar_card__UKy0n .SearchBar_cardInner__Hx4Cq .SearchBar_suggestionContainer__doJGu .SearchBar_listItemInner__eqFOY .SearchBar_discriptionBox__wZZwS {
    width: calc(100% - 56px)
}

.SearchBar_dialog__UYRLM .SearchBar_card__UKy0n .SearchBar_cardInner__Hx4Cq .SearchBar_suggestionContainer__doJGu .SearchBar_listItemInner__eqFOY .SearchBar_discriptionBox__wZZwS .SearchBar_appTitle__3qsuH {
    position: relative;
    display: flex;
    align-items: center;
    font-size: 16px;
    line-height: 24px;
    font-weight: 700;
    text-align: left;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap
}

.SearchBar_dialog__UYRLM .SearchBar_card__UKy0n .SearchBar_cardInner__Hx4Cq .SearchBar_suggestionContainer__doJGu .SearchBar_listItemInner__eqFOY .SearchBar_discriptionBox__wZZwS .SearchBar_appTitle__3qsuH .SearchBar_tag__nBNde {
    display: flex;
    align-items: center;
    width: -moz-max-content;
    width: max-content;
    height: 20px;
    padding: 2px 6px;
    border-radius: 4px;
    background-color: #3e3e3e;
    font-size: 12px;
    line-height: 16px;
    font-weight: 400;
    color: #d4d4d4
}

.SearchBar_dialog__UYRLM .SearchBar_card__UKy0n .SearchBar_cardInner__Hx4Cq .SearchBar_suggestionContainer__doJGu .SearchBar_listItemInner__eqFOY .SearchBar_discriptionBox__wZZwS .SearchBar_appDescription__hJ3Gr {
    margin-top: 4px;
    font-size: 12px;
    line-height: 16px;
    text-align: left;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
    color: #7e7e7e
}

.SearchBar_dialog__UYRLM .SearchBar_card__UKy0n .SearchBar_cardInner__Hx4Cq .SearchBar_suggestionContainer__doJGu .SearchBar_listItemInner__eqFOY .SearchBar_discriptionBox__wZZwS .SearchBar_ocrSearchText__s2sW8 {
    font-size: 14px;
    line-height: 20px;
    text-align: left
}

@media screen and (min-width: 768px) {
    .SearchBar_dialog__UYRLM .SearchBar_card__UKy0n .SearchBar_cardInner__Hx4Cq .SearchBar_suggestionContainer__doJGu .SearchBar_listItemInner__eqFOY {
        transition:all .2s
    }

    .SearchBar_dialog__UYRLM .SearchBar_card__UKy0n .SearchBar_cardInner__Hx4Cq .SearchBar_suggestionContainer__doJGu .SearchBar_listItemInner__eqFOY:hover {
        background-color: #2e2e2e;
        border-radius: 12px;
        transition: all .2s
    }
}

.SearchBar_dialog__UYRLM .SearchBar_card__UKy0n .SearchBar_cardInner__Hx4Cq .SearchBar_suggestionContainer__doJGu .SearchBar_emptyState__5ewiI {
    padding: 16px;
    border-top: 1px solid #2e2e2e;
    font-size: 14px;
    line-height: 20px
}

.SearchBar_dialog__UYRLM .SearchBar_card__UKy0n .SearchBar_cardInner__Hx4Cq .SearchBar_suggestionContainer__doJGu .SearchBar_emptyState__5ewiI>div {
    color: #a0a0a0
}

.VisualSearchPanel_textGray200___pcwO {
    color: #d4d4d4
}

.VisualSearchPanel_borderGray900__rIyBY {
    border-color: #2e2e2e
}

.VisualSearchPanel_modalBackground__w_0Gz {
    position: fixed;
    inset: 0;
    margin: auto;
    background-color: rgba(0,0,0,.75);
    z-index: 8999
}

.VisualSearchPanel_dialog__W5fVQ {
    position: fixed;
    inset: 0;
    margin: auto;
    z-index: 9000;
    pointer-events: none
}

.VisualSearchPanel_dialog__W5fVQ .VisualSearchPanel_card__ismSH {
    position: fixed;
    inset: 0;
    margin: 32px auto auto;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    width: calc(100% - 32px);
    height: -moz-max-content;
    height: max-content;
    background-color: #232323;
    border: 1px solid #2e2e2e;
    border-radius: 16px;
    pointer-events: all;
    overflow: scroll
}

@media screen and (min-width: 1024px) {
    .VisualSearchPanel_dialog__W5fVQ .VisualSearchPanel_card__ismSH {
        width:640px
    }
}

.VisualSearchPanel_dialog__W5fVQ .VisualSearchPanel_card__ismSH .VisualSearchPanel_cardTitle__5tua8 {
    display: flex;
    align-items: center;
    gap: 8px;
    width: 100%;
    height: 48px;
    padding: 0 16px;
    border-bottom: 1px solid #2e2e2e;
    font-weight: 700
}

.VisualSearchPanel_dialog__W5fVQ .VisualSearchPanel_card__ismSH .VisualSearchPanel_cardInner__5MsUm {
    width: 100%;
    padding: 24px
}

.VisualSearchPanel_dialog__W5fVQ .VisualSearchPanel_card__ismSH .VisualSearchPanel_cardInner__5MsUm .VisualSearchPanel_dropArea___K8AY {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 12px;
    min-height: 204px;
    padding: 24px;
    background-color: #2e2e2e;
    border: 2px dashed #3e3e3e;
    border-radius: 10px;
    transition: background-color .2s ease
}

.VisualSearchPanel_dialog__W5fVQ .VisualSearchPanel_card__ismSH .VisualSearchPanel_cardInner__5MsUm .VisualSearchPanel_dropArea___K8AY.VisualSearchPanel_dragging__hq7r3 {
    background-color: #3e3e3e;
    border-color: #707070
}

.VisualSearchPanel_dialog__W5fVQ .VisualSearchPanel_card__ismSH .VisualSearchPanel_cardInner__5MsUm .VisualSearchPanel_dropArea___K8AY .VisualSearchPanel_instruction__MtGjr {
    font-size: 16px;
    line-height: 24px;
    font-weight: 700
}

.VisualSearchPanel_dialog__W5fVQ .VisualSearchPanel_card__ismSH .VisualSearchPanel_cardInner__5MsUm .VisualSearchPanel_dropArea___K8AY .VisualSearchPanel_sub__pZLmR {
    font-size: 12px;
    line-height: 16px;
    color: #a0a0a0
}

.VisualSearchPanel_dialog__W5fVQ .VisualSearchPanel_card__ismSH .VisualSearchPanel_cardInner__5MsUm .VisualSearchPanel_dropArea___K8AY .VisualSearchPanel_uploadButton__UPOA6 {
    display: inline-block;
    padding: 8px 16px;
    background-color: #3e3e3e;
    border: 1px solid #505050;
    transition: .2s;
    border-radius: 50px;
    cursor: pointer;
    font-size: 14px;
    font-weight: 700
}

.VisualSearchPanel_dialog__W5fVQ .VisualSearchPanel_card__ismSH .VisualSearchPanel_cardInner__5MsUm .VisualSearchPanel_dropArea___K8AY .VisualSearchPanel_uploadButton__UPOA6:active {
    background-color: #343434
}

.VisualSearchPanel_dialog__W5fVQ .VisualSearchPanel_card__ismSH .VisualSearchPanel_cardInner__5MsUm .VisualSearchPanel_dropArea___K8AY .VisualSearchPanel_uploadButton__UPOA6 input[type=file] {
    display: none
}

.VisualSearchPanel_dialog__W5fVQ .VisualSearchPanel_card__ismSH .VisualSearchPanel_cardInner__5MsUm .VisualSearchPanel_dropArea___K8AY .VisualSearchPanel_uploadButton__UPOA6:hover {
    background-color: #505050
}

.VisualSearchPanel_dialog__W5fVQ .VisualSearchPanel_card__ismSH .VisualSearchPanel_cardInner__5MsUm .VisualSearchPanel_statusText__wnYgf {
    display: flex;
    align-items: center;
    gap: 8px
}

.VisualSearchPanel_dialog__W5fVQ .VisualSearchPanel_card__ismSH .VisualSearchPanel_cardInner__5MsUm .VisualSearchPanel_statusText__wnYgf .VisualSearchPanel_loaderBox__x4u_f {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 20px;
    height: 20px
}

.VisualSearchPanel_dialog__W5fVQ .VisualSearchPanel_card__ismSH .VisualSearchPanel_cardInner__5MsUm .VisualSearchPanel_statusText__wnYgf .VisualSearchPanel_loaderBox__x4u_f .VisualSearchPanel_loader__HloB5 {
    width: 16px;
    height: 16px;
    border: 2px solid #d4d4d4;
    border-bottom-color: transparent;
    border-radius: 50%;
    display: inline-block;
    box-sizing: border-box;
    animation: VisualSearchPanel_rotation__HOB7P 1s linear infinite
}

.VisualSearchPanel_dialog__W5fVQ .VisualSearchPanel_card__ismSH .VisualSearchPanel_cardInner__5MsUm .VisualSearchPanel_statusTextSuccess__nPBee {
    display: flex;
    align-items: center;
    gap: 8px
}

@keyframes VisualSearchPanel_rotation__HOB7P {
    0% {
        transform: rotate(0deg)
    }

    to {
        transform: rotate(1turn)
    }
}

.Button_textGray200__9lmxL {
    color: #d4d4d4
}

.Button_borderGray900__OVNGr {
    border-color: #2e2e2e
}

.Button_button___0oBV {
    position: relative;
    display: flex;
    align-items: center;
    justify-content: center;
    border-radius: 100px;
    transition: .2s;
    overflow: hidden;
    cursor: pointer
}

.Button_button___0oBV:disabled {
    cursor: not-allowed;
    opacity: .5
}

.Button_button___0oBV:focus-visible {
    outline: 2px solid #fff;
    outline-offset: 2px
}

.Button_button___0oBV:active {
    transform: scale(.96);
    transition: .2s
}

.Button_button___0oBV:hover {
    transition: .2s
}

.Button_sizeXl__OzAcR {
    height: 56px;
    padding: 0 24px
}

.Button_sizeLg__bX1po {
    height: 48px;
    padding: 0 16px;
    gap: 8px
}

.Button_sizeLg__bX1po:has(.Button_leadingIcon__6TRuV) {
    padding: 0 20px 0 16px
}

.Button_sizeLg__bX1po:has(.Button_trailingIcon__euPNZ) {
    padding: 0 16px 0 20px
}

.Button_sizeLg__bX1po:not(:has(.Button_label__zZVXy)) {
    width: 48px;
    padding: 0
}

.Button_sizeLg__bX1po .Button_label__zZVXy {
    font-size: 16px;
    line-height: 24px;
    font-weight: 700;
    white-space: nowrap
}

.Button_sizeLg__bX1po .Button_leadingIcon__6TRuV,.Button_sizeLg__bX1po .Button_trailingIcon__euPNZ {
    font-size: 20px
}

.Button_sizeMd__HS39X {
    height: 40px;
    padding: 0 16px;
    gap: 8px
}

.Button_sizeMd__HS39X:has(.Button_leadingIcon__6TRuV) {
    padding: 0 16px 0 12px
}

.Button_sizeMd__HS39X:has(.Button_trailingIcon__euPNZ) {
    padding: 0 12px 0 16px
}

.Button_sizeMd__HS39X:not(:has(.Button_label__zZVXy)) {
    height: 40px;
    width: 40px;
    padding: 0
}

.Button_sizeMd__HS39X .Button_label__zZVXy {
    font-size: 16px;
    line-height: 24px;
    font-weight: 700;
    white-space: nowrap
}

.Button_sizeMd__HS39X .Button_leadingIcon__6TRuV,.Button_sizeMd__HS39X .Button_trailingIcon__euPNZ {
    font-size: 20px
}

.Button_sizeSm__D_EyP {
    height: 32px;
    padding: 0 12px;
    gap: 8px
}

.Button_sizeSm__D_EyP:has(.Button_leadingIcon__6TRuV) {
    padding: 0 14px 0 10px
}

.Button_sizeSm__D_EyP:has(.Button_trailingIcon__euPNZ) {
    padding: 0 10px 0 14px
}

.Button_sizeSm__D_EyP:not(:has(.Button_label__zZVXy)) {
    height: 32px;
    width: 32px;
    padding: 0
}

.Button_sizeSm__D_EyP .Button_label__zZVXy {
    font-size: 14px;
    line-height: 20px;
    font-weight: 700;
    white-space: nowrap
}

.Button_sizeSm__D_EyP .Button_leadingIcon__6TRuV,.Button_sizeSm__D_EyP .Button_trailingIcon__euPNZ {
    font-size: 16px
}

.Button_sizeXs__AZAF8 {
    height: 24px;
    padding: 0 8px;
    gap: 4px
}

.Button_sizeXs__AZAF8:has(.Button_leadingIcon__6TRuV) {
    padding: 0 8px 0 6px
}

.Button_sizeXs__AZAF8:has(.Button_trailingIcon__euPNZ) {
    padding: 0 6px 0 8px
}

.Button_sizeXs__AZAF8:not(:has(.Button_label__zZVXy)) {
    height: 24px;
    padding: 0
}

.Button_sizeXs__AZAF8 .Button_label__zZVXy {
    font-size: 12px;
    line-height: 16px;
    font-weight: 700;
    white-space: nowrap
}

.Button_sizeXs__AZAF8 .Button_leadingIcon__6TRuV,.Button_sizeXs__AZAF8 .Button_trailingIcon__euPNZ {
    font-size: 12px
}

.Button_colorPink__St80p {
    background-color: #ec4899
}

.Button_colorPink__St80p.Button_outlined__ISOT6 {
    background-color: #f9a8d4;
    border: 1px solid #fff
}

.Button_colorWhite__Rnh5L {
    background-color: #fff;
    color: #161616
}

.Button_colorGray__gxJaU {
    background-color: #2e2e2e
}

.Button_colorGray__gxJaU:hover {
    background-color: #3e3e3e
}

.Button_colorGray__gxJaU:active {
    background-color: #282828
}

.Button_colorGray__gxJaU.Button_blurred__9FKB1 {
    background-color: rgba(50,50,50,.5);
    border: 1px solid hsla(0,0%,100%,.1);
    backdrop-filter: blur(40px);
    -webkit-backdrop-filter: blur(40px)
}

.Button_colorGray__gxJaU.Button_blurred__9FKB1:hover {
    background-color: rgba(75,75,75,.5)
}

.Button_colorGray__gxJaU.Button_blurred__9FKB1:disabled:hover {
    background-color: rgba(50,50,50,.5)
}

.Button_colorGray__gxJaU.Button_text__s2MKv {
    background-color: transparent
}

.Button_colorGray__gxJaU.Button_text__s2MKv:hover {
    background-color: hsla(0,0%,100%,.15)
}

.Button_colorGray__gxJaU.Button_text__s2MKv:disabled:hover {
    background-color: transparent
}

.Button_colorRed__BK0ht {
    background-color: #ef4444
}

.Button_colorRed__BK0ht:hover {
    background-color: #f87171
}

.Button_colorRed__BK0ht:active {
    background-color: #ef4444
}

.Button_colorPro___qCYR {
    background-color: #fff;
    color: #161616;
    border-radius: 50px;
    transition: .2s
}

.Button_colorPro___qCYR:active {
    transform: scale(1)
}

.Button_loaderBox__lJArD {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%,-50%);
    -webkit-transform: translate(-50%,-50%);
    -ms-transform: translate(-50%,-50%);
    display: flex;
    align-items: center;
    justify-content: center;
    width: 20px;
    height: 20px
}

.Button_loaderBox__lJArD .Button_loader__wYJKr {
    width: 16px;
    height: 16px;
    border: 2px solid #d4d4d4;
    border-bottom-color: transparent;
    border-radius: 50%;
    display: inline-block;
    box-sizing: border-box;
    animation: Button_rotation__JhVal 1s linear infinite
}

.Button_loaderBox__lJArD~* {
    background-color: transparent;
    color: transparent
}

@keyframes Button_rotation__JhVal {
    0% {
        transform: rotate(0deg)
    }

    to {
        transform: rotate(1turn)
    }
}

.Button_favoriteButton__eddOu {
    position: relative;
    display: flex;
    align-items: center;
    justify-content: center;
    height: 40px;
    width: 40px;
    border-radius: 100px;
    background-color: rgba(50,50,50,.5);
    border: 1px solid hsla(0,0%,100%,.1);
    backdrop-filter: blur(40px);
    -webkit-backdrop-filter: blur(40px);
    transition: .2s;
    overflow: hidden;
    cursor: pointer
}

.Button_favoriteButton__eddOu:hover {
    background-color: rgba(75,75,75,.5)
}

.Button_favoriteButton__eddOu:disabled:hover {
    background-color: rgba(50,50,50,.5)
}

.Button_favoriteButton__eddOu:disabled {
    cursor: not-allowed;
    opacity: .5
}

.Button_favoriteButton__eddOu:focus-visible {
    outline: 2px solid #fff;
    outline-offset: 2px
}

.Button_favoriteButton__eddOu:active {
    transform: scale(.96)
}

.Button_favorited__rIOVd {
    background-color: rgba(236,72,153,.15)
}

.Button_favorited__rIOVd:hover {
    background-color: rgba(236,72,153,.25)
}

.Button_TooltipContent__3iI8q {
    background-color: rgba(46,46,46,.8);
    border: 1px solid hsla(0,0%,100%,.05);
    backdrop-filter: blur(40px);
    -webkit-backdrop-filter: blur(40px);
    box-shadow: 0 0 8px rgba(0,0,0,.5);
    padding: 4px 8px;
    font-size: 14px;
    line-height: 20px;
    border-radius: 8px;
    z-index: 999999
}

.AvatarDropdownButton_textGray200__YHx8y {
    color: #d4d4d4
}

.AvatarDropdownButton_borderGray900__7sI6d {
    border-color: #2e2e2e
}

.AvatarDropdownButton_wrapper__Stm2_ {
    display: flex;
    align-items: center;
    gap: 16px
}

.AvatarDropdownButton_avatarButton__A_xTJ {
    border-radius: 100px;
    border: 2px solid #3e3e3e;
    overflow: hidden;
    cursor: pointer
}

.AvatarDropdownButton_avatarButton__A_xTJ .AvatarDropdownButton_avatarImg__eA0wl {
    width: 32px;
    height: 32px
}

.AvatarDropdownButton_subscribed__1MCcR {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 36px;
    height: 36px;
    background: linear-gradient(138deg,#f957dc 37.44%,#72aeff 100.06%);
    border-radius: 50px
}

.AvatarDropdownButton_subscribed__1MCcR .AvatarDropdownButton_avatarButton__A_xTJ {
    border: none
}

.AvatarDropdownButton_skeltonAvatar__sbIgn {
    width: 32px;
    height: 32px;
    background: #232323;
    position: relative;
    border-radius: 50px;
    overflow: hidden
}

.AvatarDropdownButton_skeltonAvatar__sbIgn:before {
    content: "";
    display: block;
    height: 100%;
    width: 100%;
    background: linear-gradient(90deg,transparent,rgba(80,80,80,.1),transparent);
    position: absolute;
    top: 0;
    left: 0;
    animation: AvatarDropdownButton_skeleton-animation__zviuh 1.2s linear infinite
}

@keyframes AvatarDropdownButton_skeleton-animation__zviuh {
    0% {
        transform: translateX(-100%)
    }

    to {
        transform: translateX(100%)
    }
}

.GlobalHeader_textGray200__7kTeQ {
    color: #d4d4d4
}

.GlobalHeader_borderGray900__KwZ6L {
    border-color: #2e2e2e
}

.GlobalHeader_header__KVzeO {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 56px;
    background-color: #161616;
    border-bottom: 1px solid #2e2e2e;
    z-index: 900
}

.GlobalHeader_header__KVzeO .GlobalHeader_inner__Uls0l {
    position: relative;
    display: flex;
    align-items: center;
    justify-content: space-between;
    width: 100%;
    height: 100%;
    padding: 0 16px
}

.GlobalHeader_header__KVzeO .GlobalHeader_inner__Uls0l .GlobalHeader_headerLogoContainer__uVN8f {
    display: flex;
    align-items: center;
    gap: 4px
}

.GlobalHeader_header__KVzeO .GlobalHeader_inner__Uls0l .GlobalHeader_headerLogoContainer__uVN8f .GlobalHeader_separator__BiLO3 {
    width: 2px;
    height: 24px;
    margin-right: 8px;
    margin-left: 16px;
    background-color: #707070;
    transform: rotate(30deg)
}

.GlobalHeader_header__KVzeO .GlobalHeader_inner__Uls0l .GlobalHeader_logoWrapper__MuI6H {
    height: 24px;
    width: auto;
    min-width: 24px
}

.GlobalHeader_header__KVzeO .GlobalHeader_inner__Uls0l .GlobalHeader_logoWrapper__MuI6H .GlobalHeader_logo__Okfqz {
    width: 100%;
    height: 100%;
    -o-object-fit: cover;
    object-fit: cover
}

.GlobalHeader_header__KVzeO .GlobalHeader_inner__Uls0l .GlobalHeader_searchWrapper__WsWEK {
    position: relative
}

.GlobalHeader_header__KVzeO .GlobalHeader_inner__Uls0l .GlobalHeader_searchWrapper__WsWEK .GlobalHeader_searchButton__ZcRU4 {
    display: none
}

@media screen and (min-width: 1024px) {
    .GlobalHeader_header__KVzeO .GlobalHeader_inner__Uls0l .GlobalHeader_searchWrapper__WsWEK .GlobalHeader_searchButton__ZcRU4 {
        display:flex;
        gap: 8px;
        width: 480px;
        height: 36px;
        padding: 8px;
        background-color: #232323;
        align-items: center;
        justify-content: flex-start;
        border: 1px solid #2e2e2e;
        border-radius: 10px;
        transition: all .2s
    }

    .GlobalHeader_header__KVzeO .GlobalHeader_inner__Uls0l .GlobalHeader_searchWrapper__WsWEK .GlobalHeader_searchButton__ZcRU4:hover {
        background-color: #2e2e2e;
        transition: all .2s
    }

    .GlobalHeader_header__KVzeO .GlobalHeader_inner__Uls0l .GlobalHeader_searchWrapper__WsWEK .GlobalHeader_searchButton__ZcRU4 .GlobalHeader_searchButtonLabel__aLLZo {
        display: flex;
        align-items: center;
        gap: 8px
    }

    .GlobalHeader_header__KVzeO .GlobalHeader_inner__Uls0l .GlobalHeader_searchWrapper__WsWEK .GlobalHeader_searchButton__ZcRU4 .GlobalHeader_searchButtonLabel__aLLZo span {
        color: #d4d4d4;
        font-size: 14px;
        line-height: 20px
    }

    .GlobalHeader_header__KVzeO .GlobalHeader_inner__Uls0l .GlobalHeader_searchWrapper__WsWEK .GlobalHeader_searchButton__ZcRU4 .GlobalHeader_searchButtonLabel__aLLZo .GlobalHeader_label__gFhy5 {
        display: flex;
        align-items: center;
        width: -moz-max-content;
        width: max-content;
        padding: 0 4px;
        height: 18px;
        border-radius: 4px;
        background: linear-gradient(138deg,#ec4884 37.44%,#b352d1 100.06%);
        font-size: 12px;
        line-height: 16px;
        font-weight: 700
    }
}

.GlobalHeader_header__KVzeO .GlobalHeader_inner__Uls0l .GlobalHeader_searchWrapper__WsWEK .GlobalHeader_searchButton__ZcRU4:focus {
    outline: none
}

.GlobalHeader_header__KVzeO .GlobalHeader_inner__Uls0l .GlobalHeader_searchWrapper__WsWEK .GlobalHeader_searchButton__ZcRU4:focus-visible {
    outline: 2px solid #fff;
    outline-offset: 2px
}

.GlobalHeader_header__KVzeO .GlobalHeader_inner__Uls0l .GlobalHeader_searchWrapper__WsWEK .GlobalHeader_searchButtonSm__StrsB {
    padding: 8px;
    color: #a0a0a0
}

.GlobalHeader_header__KVzeO .GlobalHeader_inner__Uls0l .GlobalHeader_searchWrapper__WsWEK .GlobalHeader_visualSearchButton__rIZbH {
    display: none
}

@media screen and (min-width: 1024px) {
    .GlobalHeader_header__KVzeO .GlobalHeader_inner__Uls0l .GlobalHeader_searchWrapper__WsWEK .GlobalHeader_visualSearchButton__rIZbH {
        position:absolute;
        top: 4px;
        right: 4px;
        width: 28px;
        height: 28px;
        display: flex;
        align-items: center;
        justify-content: center;
        border-radius: 8px;
        cursor: pointer;
        z-index: 99;
        transition: .2s
    }

    .GlobalHeader_header__KVzeO .GlobalHeader_inner__Uls0l .GlobalHeader_searchWrapper__WsWEK .GlobalHeader_visualSearchButton__rIZbH:hover {
        background-color: #343434
    }

    .GlobalHeader_header__KVzeO .GlobalHeader_inner__Uls0l .GlobalHeader_searchWrapper__WsWEK .GlobalHeader_visualSearchButton__rIZbH:active {
        transform: scale(.95);
        transition: .2s
    }

    .GlobalHeader_header__KVzeO .GlobalHeader_inner__Uls0l .GlobalHeader_searchWrapper__WsWEK .GlobalHeader_visualSearchButton__rIZbH:focus-visible {
        outline: 2px solid #fff;
        outline-offset: 2px
    }
}

.GlobalHeader_header__KVzeO .GlobalHeader_inner__Uls0l .GlobalHeader_headerNav__113TR {
    display: flex;
    align-items: center
}

.GlobalHeader_header__KVzeO .GlobalHeader_inner__Uls0l .GlobalHeader_headerNav__113TR .GlobalHeader_searchButtonSm__StrsB {
    display: flex
}

@media screen and (min-width: 1024px) {
    .GlobalHeader_header__KVzeO .GlobalHeader_inner__Uls0l .GlobalHeader_headerNav__113TR .GlobalHeader_searchButtonSm__StrsB {
        display:none
    }
}

.GlobalSidebar_textGray200__Yhfof {
    color: #d4d4d4
}

.GlobalSidebar_borderGray900__O84Dh {
    border-color: #2e2e2e
}

.GlobalSidebar_globalSidebar__C2zFe {
    position: fixed;
    bottom: 0;
    left: 0;
    width: 100%;
    padding-bottom: env(safe-area-inset-bottom)!important;
    background-color: #161616;
    border-top: 1px solid #232323;
    z-index: 850
}

@media screen and (min-width: 1024px) {
    .GlobalSidebar_globalSidebar__C2zFe {
        top:56px;
        left: 0;
        width: 56px;
        height: calc(100vh - 56px);
        border-right: 1px solid #2e2e2e;
        border-top: 0;
        transition: all .2s ease-out
    }

    .GlobalSidebar_globalSidebar__C2zFe * {
        transition: all .2s ease-out
    }

    .GlobalSidebar_globalSidebar__C2zFe .GlobalSidebar_globalNavText__g7x17 {
        opacity: 0;
        position: absolute;
        left: 16px;
        font-size: 14px;
        line-height: 20px;
        width: 128px
    }

    .GlobalSidebar_globalSidebar__C2zFe:has(.GlobalSidebar_menuOpen__fRmzN) {
        width: 192px
    }
}

.GlobalSidebar_globalSidebar__C2zFe .GlobalSidebar_inner__DeCKv {
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: space-around;
    width: 100%;
    height: 100%;
    padding: 8px 16px
}

@media screen and (min-width: 1024px) {
    .GlobalSidebar_globalSidebar__C2zFe .GlobalSidebar_inner__DeCKv {
        flex-direction:column;
        align-items: flex-start;
        justify-content: flex-start;
        gap: 16px;
        width: 100%;
        height: 100%;
        padding: 8px
    }

    .GlobalSidebar_globalSidebar__C2zFe .GlobalSidebar_menuOpen__fRmzN {
        width: 192px
    }
}

.GlobalSidebar_globalSidebar__C2zFe .GlobalSidebar_menuOpen__fRmzN .GlobalSidebar_globalNavText__g7x17 {
    opacity: 1;
    left: 40px;
    width: 128px;
    font-size: 14px;
    line-height: 20px
}

.GlobalSidebar_globalSidebar__C2zFe .GlobalSidebar_globalNavList__dc7T5 {
    display: flex;
    flex-direction: row;
    justify-content: space-around;
    gap: 8px;
    width: 100%
}

@media screen and (min-width: 1024px) {
    .GlobalSidebar_globalSidebar__C2zFe .GlobalSidebar_globalNavList__dc7T5 {
        flex-direction:column;
        justify-content: flex-start
    }
}

.GlobalSidebar_globalSidebar__C2zFe .GlobalSidebar_globalNavList__dc7T5 .GlobalSidebar_divider__ZFloN {
    display: none
}

@media screen and (min-width: 1024px) {
    .GlobalSidebar_globalSidebar__C2zFe .GlobalSidebar_globalNavList__dc7T5 .GlobalSidebar_divider__ZFloN {
        display:block;
        border-top: 1px solid #2e2e2e
    }
}

.GlobalSidebar_globalSidebar__C2zFe .GlobalSidebar_globalNavList__dc7T5 .GlobalSidebar_listItem__7jhC_ .GlobalSidebar_listItemInner__SyfhD {
    position: relative;
    display: flex;
    align-items: center;
    gap: 8px;
    min-width: 40px;
    padding: 10px;
    border-radius: 6px;
    overflow: hidden
}

.GlobalSidebar_globalSidebar__C2zFe .GlobalSidebar_globalNavList__dc7T5 .GlobalSidebar_listItem__7jhC_ .GlobalSidebar_listItemInner__SyfhD .GlobalSidebar_icon__iDIBH {
    fill: #7e7e7e
}

.GlobalSidebar_globalSidebar__C2zFe .GlobalSidebar_globalNavList__dc7T5 .GlobalSidebar_listItem__7jhC_ .GlobalSidebar_listItemInner__SyfhD .GlobalSidebar_globalNavText__g7x17 {
    display: none;
    color: #7e7e7e
}

@media screen and (min-width: 1024px) {
    .GlobalSidebar_globalSidebar__C2zFe .GlobalSidebar_globalNavList__dc7T5 .GlobalSidebar_listItem__7jhC_ .GlobalSidebar_listItemInner__SyfhD .GlobalSidebar_globalNavText__g7x17 {
        display:block
    }
}

.GlobalSidebar_globalSidebar__C2zFe .GlobalSidebar_globalNavList__dc7T5 .GlobalSidebar_listItem__7jhC_ .GlobalSidebar_listItemInner__SyfhD:hover {
    background-color: #232323
}

.GlobalSidebar_globalSidebar__C2zFe .GlobalSidebar_globalNavList__dc7T5 .GlobalSidebar_listItem__7jhC_ .GlobalSidebar_listItemInner__SyfhD:hover .GlobalSidebar_icon__iDIBH {
    fill: #fff
}

.GlobalSidebar_globalSidebar__C2zFe .GlobalSidebar_globalNavList__dc7T5 .GlobalSidebar_listItem__7jhC_ .GlobalSidebar_listItemInner__SyfhD:hover .GlobalSidebar_globalNavText__g7x17 {
    color: #fff
}

.GlobalSidebar_globalSidebar__C2zFe .GlobalSidebar_globalNavList__dc7T5 .GlobalSidebar_listItem__7jhC_ .GlobalSidebar_active__0vn_O {
    background-color: #232323
}

.GlobalSidebar_globalSidebar__C2zFe .GlobalSidebar_globalNavList__dc7T5 .GlobalSidebar_listItem__7jhC_ .GlobalSidebar_active__0vn_O .GlobalSidebar_icon__iDIBH {
    fill: #fff
}

.GlobalSidebar_globalSidebar__C2zFe .GlobalSidebar_globalNavList__dc7T5 .GlobalSidebar_listItem__7jhC_ .GlobalSidebar_active__0vn_O .GlobalSidebar_globalNavText__g7x17 {
    color: #fff
}

.GlobalFooter_textGray200__JcvUo {
    color: #d4d4d4
}

.GlobalFooter_borderGray900__rJwXR {
    border-color: #2e2e2e
}

.GlobalFooter_footer__oaHOl {
    width: 100%;
    height: -moz-max-content;
    height: max-content;
    background-color: #161616;
    border-top: 1px solid #2e2e2e;
    margin-bottom: 56px;
    padding: 0 16px
}

@media screen and (min-width: 1024px) {
    .GlobalFooter_footer__oaHOl {
        width:calc(100% - 56px);
        margin-left: 56px;
        margin-bottom: 0;
        padding: 0
    }
}

.GlobalFooter_footer__oaHOl .GlobalFooter_inner__jFAKN {
    display: flex;
    align-items: flex-start;
    flex-direction: column;
    width: 100%;
    padding: 64px 0
}

@media screen and (min-width: 1024px) {
    .GlobalFooter_footer__oaHOl .GlobalFooter_inner__jFAKN {
        gap:64px;
        margin: auto;
        padding: 64px 32px
    }
}

@media screen and (min-width: 1280px) {
    .GlobalFooter_footer__oaHOl .GlobalFooter_inner__jFAKN {
        flex-direction:row;
        justify-content: space-between;
        gap: 0
    }
}

.GlobalFooter_footer__oaHOl .GlobalFooter_inner__jFAKN .GlobalFooter_logoBox__CxagM {
    height: 32px;
    display: flex;
    align-items: center
}

.GlobalFooter_footer__oaHOl .GlobalFooter_inner__jFAKN .GlobalFooter_footerMenuWrapper__0tq7L {
    display: flex;
    flex-wrap: wrap;
    gap: 16px;
    width: 100%;
    margin-top: 32px
}

@media screen and (min-width: 1024px) {
    .GlobalFooter_footer__oaHOl .GlobalFooter_inner__jFAKN .GlobalFooter_footerMenuWrapper__0tq7L {
        gap:0;
        margin-top: 0;
        flex-wrap: nowrap;
        width: -moz-max-content;
        width: max-content
    }

    .GlobalFooter_footer__oaHOl .GlobalFooter_inner__jFAKN .GlobalFooter_footerMenuWrapper__0tq7L .GlobalFooter_menuGroupContainer__f2xcb {
        width: 224px
    }
}

.GlobalFooter_footer__oaHOl .GlobalFooter_inner__jFAKN .GlobalFooter_footerMenuWrapper__0tq7L .GlobalFooter_menuGroupContainer__f2xcb .GlobalFooter_menuTitle___NW75 {
    font-size: 14px;
    line-height: 20px;
    font-weight: 700
}

.GlobalFooter_footer__oaHOl .GlobalFooter_inner__jFAKN .GlobalFooter_footerMenuWrapper__0tq7L .GlobalFooter_menuGroupContainer__f2xcb .GlobalFooter_menuTitle___NW75 a {
    width: -moz-max-content;
    width: max-content;
    font-size: 14px;
    line-height: 20px;
    font-weight: 700;
    transition: .2s
}

.GlobalFooter_footer__oaHOl .GlobalFooter_inner__jFAKN .GlobalFooter_footerMenuWrapper__0tq7L .GlobalFooter_menuGroupContainer__f2xcb .GlobalFooter_menuTitle___NW75 a:hover {
    color: #fff;
    transition: .2s
}

.GlobalFooter_footer__oaHOl .GlobalFooter_inner__jFAKN .GlobalFooter_footerMenuWrapper__0tq7L .GlobalFooter_menuGroupContainer__f2xcb .GlobalFooter_menuList__gRiv5 .GlobalFooter_listItem__y2Vb4 {
    margin-top: 16px
}

.GlobalFooter_footer__oaHOl .GlobalFooter_inner__jFAKN .GlobalFooter_footerMenuWrapper__0tq7L .GlobalFooter_menuGroupContainer__f2xcb .GlobalFooter_menuList__gRiv5 .GlobalFooter_listItem__y2Vb4 a {
    display: inline;
    font-size: 14px;
    line-height: 20px;
    color: #a0a0a0;
    transition: .2s
}

@media screen and (min-width: 1024px) {
    .GlobalFooter_footer__oaHOl .GlobalFooter_inner__jFAKN .GlobalFooter_footerMenuWrapper__0tq7L .GlobalFooter_menuGroupContainer__f2xcb .GlobalFooter_menuList__gRiv5 .GlobalFooter_listItem__y2Vb4 a {
        display:inline-flex;
        align-items: center
    }
}

.GlobalFooter_footer__oaHOl .GlobalFooter_inner__jFAKN .GlobalFooter_footerMenuWrapper__0tq7L .GlobalFooter_menuGroupContainer__f2xcb .GlobalFooter_menuList__gRiv5 .GlobalFooter_listItem__y2Vb4 a .GlobalFooter_icon__7mIOC {
    display: inline-block;
    margin-left: 2px;
    margin-bottom: 2px;
    color: #a0a0a0
}

.GlobalFooter_footer__oaHOl .GlobalFooter_inner__jFAKN .GlobalFooter_footerMenuWrapper__0tq7L .GlobalFooter_menuGroupContainer__f2xcb .GlobalFooter_menuList__gRiv5 .GlobalFooter_listItem__y2Vb4 a:hover {
    color: #ededed;
    transition: .2s
}

.GlobalFooter_footer__oaHOl .GlobalFooter_inner__jFAKN .GlobalFooter_footerMenuWrapper__0tq7L .GlobalFooter_menuGroupContainer__f2xcb .GlobalFooter_menuList__gRiv5 .GlobalFooter_listItem__y2Vb4 a:hover * {
    color: #ec4899;
    transition: .2s
}

.GlobalFooter_footer__oaHOl .GlobalFooter_inner__jFAKN .GlobalFooter_footerMenuWrapper__0tq7L .GlobalFooter_menuGroupContainer__f2xcb {
    display: flex;
    flex-wrap: wrap;
    align-items: flex-start;
    width: 100%;
    margin-top: 16px;
    gap: 16px
}

@media screen and (min-width: 1024px) {
    .GlobalFooter_footer__oaHOl .GlobalFooter_inner__jFAKN .GlobalFooter_footerMenuWrapper__0tq7L .GlobalFooter_menuGroupContainer__f2xcb {
        width:-moz-max-content;
        width: max-content;
        gap: 0
    }
}

.GlobalFooter_footer__oaHOl .GlobalFooter_inner__jFAKN .GlobalFooter_footerMenuWrapper__0tq7L .GlobalFooter_menuGroupContainer__f2xcb .GlobalFooter_menuBox__UnPLc {
    width: calc(50% - 8px)
}

@media screen and (min-width: 1024px) {
    .GlobalFooter_footer__oaHOl .GlobalFooter_inner__jFAKN .GlobalFooter_footerMenuWrapper__0tq7L .GlobalFooter_menuGroupContainer__f2xcb .GlobalFooter_menuBox__UnPLc {
        width:224px
    }

    .GlobalFooter_footer__oaHOl .GlobalFooter_inner__jFAKN .GlobalFooter_footerMenuWrapper__0tq7L .GlobalFooter_menuGroupContainer__f2xcb {
        margin-top: 0;
        flex-direction: column;
        gap: 32px
    }

    .GlobalFooter_footer__oaHOl .GlobalFooter_inner__jFAKN .GlobalFooter_footerMenuWrapper__0tq7L .GlobalFooter_menuGroupContainer__f2xcb .GlobalFooter_menuBox__UnPLc:last-child {
        margin-top: 0
    }
}

.GlobalFooter_footer__oaHOl .GlobalFooter_copyright__QEuyb {
    display: flex;
    align-items: center;
    justify-content: space-between;
    height: 64px;
    padding: 0 16px
}

@media screen and (min-width: 1024px) {
    .GlobalFooter_footer__oaHOl .GlobalFooter_copyright__QEuyb {
        margin:0 32px;
        padding: 0
    }
}

.GlobalFooter_footer__oaHOl .GlobalFooter_copyright__QEuyb span {
    font-size: 14px;
    line-height: 20px;
    color: #a0a0a0
}

@media screen and (min-width: 1024px) {
    .GlobalFooter_haveLocalSidebar__VZHQn {
        width:calc(100% - 328px);
        margin-left: 328px
    }
}

.Sheet_textGray200__p4fQC {
    color: #d4d4d4
}

.Sheet_borderGray900__xvz0d {
    border-color: #2e2e2e
}

.Sheet_modalBackground__LMGrG {
    position: fixed;
    inset: 0;
    background-color: rgba(0,0,0,.5);
    z-index: 1000
}

.Sheet_sheetWrapper__4LwrG {
    position: fixed;
    inset: 0;
    display: flex;
    justify-content: center;
    align-items: flex-end;
    z-index: 1010;
    pointer-events: none
}

@media screen and (min-width: 1024px) {
    .Sheet_sheetWrapper__4LwrG {
        align-items:center
    }
}

.Sheet_sheet__bBX_v {
    width: 100%;
    background-color: #232323;
    border-radius: 12px 12px 0 0;
    border-top: 1px solid #2e2e2e;
    box-shadow: 0 -4px 24px rgba(0,0,0,.25);
    overflow: scroll;
    pointer-events: all
}

@media screen and (min-width: 1024px) {
    .Sheet_sheet__bBX_v {
        border-radius:12px;
        border: 1px solid #2e2e2e
    }
}

.Sheet_sheetMd__JII_6 {
    height: -moz-max-content;
    height: max-content
}

@media screen and (min-width: 1024px) {
    .Sheet_sheetMd__JII_6 {
        width:528px
    }
}

.Sheet_sheetLg__dD4jU {
    height: 90%
}

.Sheet_sheetFull__Djm2a {
    height: 100%;
    border-radius: 0
}

.SignUpInSheet_textGray200__zaB8k {
    color: #d4d4d4
}

.SignUpInSheet_borderGray900__YCxvF {
    border-color: #2e2e2e
}

.SignUpInSheet_sheetInner__vifUD {
    padding: 24px
}

.SignUpInSheet_sheetInner__vifUD .SignUpInSheet_titleWrapper__06PGW {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 32px
}

.SignUpInSheet_sheetInner__vifUD .SignUpInSheet_titleWrapper__06PGW .SignUpInSheet_logo__ytFUH {
    width: auto;
    height: 32px
}

.SignUpInSheet_sheetInner__vifUD .SignUpInSheet_titleWrapper__06PGW .SignUpInSheet_cardTitle__2qTkN {
    font-size: 20px;
    line-height: 28px;
    font-weight: 700
}

.SignUpInSheet_sheetInner__vifUD .SignUpInSheet_description__eElMA {
    font-size: 12px;
    line-height: 16px;
    color: #7e7e7e;
    text-align: center
}

.SignUpInSheet_sheetInner__vifUD .SignUpInSheet_description__eElMA .SignUpInSheet_textLink__PLSRT {
    display: inline;
    text-decoration: underline
}

.SignUpInSheet_sheetInner__vifUD .SignUpInSheet_alert__RjVfH {
    display: flex;
    gap: 8px;
    padding: 12px;
    border-radius: 6px;
    background-color: rgba(33,94,250,.125)
}

.SignUpInSheet_sheetInner__vifUD .SignUpInSheet_alert__RjVfH .SignUpInSheet_icon__i9sGb {
    color: #60a5fa
}

.SignUpInSheet_sheetInner__vifUD .SignUpInSheet_alert__RjVfH .SignUpInSheet_alertDescription__7jvxE {
    display: inline-block;
    width: calc(100% - 28px);
    text-align: left;
    font-size: 14px;
    line-height: 20px;
    color: #60a5fa
}

.PaywallSheet_textGray200__DkBPy {
    color: #d4d4d4
}

.PaywallSheet_borderGray900__m5oFR {
    border-color: #2e2e2e
}

.PaywallSheet_thumbnailBox__mfYe8 {
    position: relative;
    display: flex;
    align-items: center;
    justify-content: center;
    aspect-ratio: 2/1;
    background: linear-gradient(180deg,#f571e8,#7cc5e5);
    border-bottom: 1px solid #2e2e2e
}

.PaywallSheet_descriptionBox__AtCAN {
    padding: 24px
}

.PaywallSheet_descriptionBox__AtCAN .PaywallSheet_sheetTitle__RJdx5 {
    font-size: 24px;
    line-height: 32px;
    font-weight: 700
}

.PaywallSheet_descriptionBox__AtCAN .PaywallSheet_sheetDescription__KQ1FS {
    font-size: 16px;
    line-height: 24px
}

.TextInput_textGray200__m93Mc {
    color: #d4d4d4
}

.TextInput_borderGray900__hF7rC {
    border-color: #2e2e2e
}

.TextInput_textInputWrapper___QvVU {
    display: flex;
    flex-direction: column
}

.TextInput_textInputWrapper___QvVU .TextInput_textInputLabel__ZmTZd {
    display: flex;
    align-items: center;
    gap: 8px;
    font-size: 14px;
    line-height: 20px;
    color: #fff
}

.TextInput_textInputWrapper___QvVU .TextInput_textInputLabel__ZmTZd .TextInput_requiredLabel__ZQnDP {
    padding: 2px 6px;
    background-color: #ef4444;
    border-radius: 4px;
    font-size: 10px;
    line-height: 12px;
    font-weight: 700;
    color: #fff
}

.TextInput_textInputWrapper___QvVU .TextInput_textInputLabel__ZmTZd .TextInput_optionalLabel__RFy18 {
    padding: 2px 6px;
    background-color: #3e3e3e;
    border-radius: 4px;
    font-size: 10px;
    line-height: 12px;
    font-weight: 700;
    color: #d4d4d4
}

.TextInput_textInputWrapper___QvVU .TextInput_textInput__KkC2H {
    align-items: center;
    justify-content: center;
    width: 100%;
    background-color: hsla(0,0%,100%,.1);
    border: 1px solid hsla(0,0%,100%,.05);
    transition: all .2s
}

.TextInput_textInputWrapper___QvVU .TextInput_textInput__KkC2H::-moz-placeholder {
    color: #a0a0a0
}

.TextInput_textInputWrapper___QvVU .TextInput_textInput__KkC2H::placeholder {
    color: #a0a0a0
}

.TextInput_textInputWrapper___QvVU .TextInput_textInput__KkC2H:disabled {
    color: #707070;
    cursor: not-allowed
}

.TextInput_textInputWrapper___QvVU .TextInput_textInput__KkC2H.TextInput_error___eYDa {
    border-color: #ef4444;
    background-color: rgba(239,68,68,.15)
}

.TextInput_textInputWrapper___QvVU.TextInput_sm__hXCU5 .TextInput_textInput__KkC2H {
    height: 32px;
    padding: 6px 8px;
    border-radius: 6px;
    font-size: 14px;
    line-height: 20px
}

.TextInput_textInputWrapper___QvVU.TextInput_sm__hXCU5 .TextInput_textInput__KkC2H:focus {
    border: 1px solid #707070;
    box-shadow: 0 0 0 2px hsla(0,0%,100%,.1);
    transition: all .2s
}

.TextInput_textInputWrapper___QvVU.TextInput_md__sUbEK .TextInput_textInput__KkC2H {
    height: 40px;
    padding: 8px 12px;
    border-radius: 8px;
    font-size: 16px;
    line-height: 24px
}

.TextInput_textInputWrapper___QvVU.TextInput_md__sUbEK .TextInput_textInput__KkC2H:focus {
    border: 1px solid hsla(0,0%,100%,.5);
    box-shadow: 0 0 0 4px hsla(0,0%,100%,.2);
    transition: all .2s
}

.TextInput_textInputWrapper___QvVU .TextInput_formErrorMessage__JY_Pb {
    font-size: 12px;
    line-height: 16px;
    color: #ef4444
}

.TextInput_error___eYDa:focus {
    border: 1px solid #ef4444!important;
    box-shadow: 0 0 0 4px rgba(239,68,68,.4)!important;
    transition: all .2s
}

.TextInput_textarea__tSV2k {
    min-height: 128px;
    padding: 8px 12px;
    border-radius: 8px
}

.TextInput_textarea__tSV2k:focus {
    border: 1px solid hsla(0,0%,100%,.5);
    box-shadow: 0 0 0 4px hsla(0,0%,100%,.2);
    transition: all .2s
}

.SelectInput_textGray200__rRXX8 {
    color: #d4d4d4
}

.SelectInput_borderGray900___P3RA {
    border-color: #2e2e2e
}

.SelectInput_textInputWrapper__KPlHy {
    display: flex;
    flex-direction: column;
    cursor: pointer
}

.SelectInput_textInputWrapper__KPlHy .SelectInput_textInputLabel__B_PkN {
    display: flex;
    align-items: center;
    gap: 8px;
    font-size: 14px;
    line-height: 20px;
    color: #fff
}

.SelectInput_textInputWrapper__KPlHy .SelectInput_textInputLabel__B_PkN .SelectInput_requiredLabel__k4Kd8 {
    padding: 2px 6px;
    background-color: #ef4444;
    border-radius: 4px;
    font-size: 10px;
    line-height: 12px;
    font-weight: 700;
    color: #fff
}

.SelectInput_textInputWrapper__KPlHy .SelectInput_textInputLabel__B_PkN .SelectInput_optionalLabel__zgCNx {
    padding: 2px 6px;
    background-color: #3e3e3e;
    border-radius: 4px;
    font-size: 10px;
    line-height: 12px;
    font-weight: 700;
    color: #d4d4d4
}

.SelectInput_textInputWrapper__KPlHy .SelectInput_textInput__7_Q0q {
    align-items: center;
    justify-content: center;
    width: 100%;
    height: 32px;
    padding: 6px 8px;
    background-color: hsla(0,0%,100%,.1);
    border: 1px solid hsla(0,0%,100%,.05);
    transition: all .2s
}

.SelectInput_textInputWrapper__KPlHy .SelectInput_textInput__7_Q0q::-moz-placeholder {
    color: #707070
}

.SelectInput_textInputWrapper__KPlHy .SelectInput_textInput__7_Q0q::placeholder {
    color: #707070
}

.SelectInput_textInputWrapper__KPlHy .SelectInput_textInput__7_Q0q:focus {
    border: 1px solid #707070;
    box-shadow: 0 0 0 2px hsla(0,0%,100%,.1);
    transition: all .2s
}

.SelectInput_textInputWrapper__KPlHy .SelectInput_textInput__7_Q0q:disabled {
    color: #707070;
    cursor: not-allowed
}

.SelectInput_textInputWrapper__KPlHy .SelectInput_textInput__7_Q0q .SelectInput_textInputBox__Exh3j {
    position: relative
}

.SelectInput_textInputWrapper__KPlHy.SelectInput_sm__pQxuF .SelectInput_textInput__7_Q0q {
    height: 32px;
    padding: 6px 8px;
    border-radius: 6px;
    font-size: 14px;
    line-height: 20px
}

.SelectInput_textInputWrapper__KPlHy.SelectInput_sm__pQxuF .SelectInput_textInput__7_Q0q:focus {
    border: 1px solid #707070;
    box-shadow: 0 0 0 2px hsla(0,0%,100%,.1);
    transition: all .2s
}

.SelectInput_textInputWrapper__KPlHy.SelectInput_md__OnNYi .SelectInput_textInput__7_Q0q {
    height: 40px;
    padding: 8px 12px;
    border-radius: 8px;
    font-size: 16px;
    line-height: 24px
}

.SelectInput_textInputWrapper__KPlHy.SelectInput_md__OnNYi .SelectInput_textInput__7_Q0q:focus {
    border: 1px solid hsla(0,0%,100%,.5);
    box-shadow: 0 0 0 4px hsla(0,0%,100%,.2);
    transition: all .2s
}

.SelectInput_textInputWrapper__KPlHy .SelectInput_formErrorMessage__K2LDo {
    font-size: 12px;
    line-height: 16px;
    color: #ef4444
}

.SelectInput_textInputWrapper__KPlHy .SelectInput_icon__zrMlr {
    position: absolute;
    top: 50%;
    transform: translateY(-50%);
    -webkit-transform: translateY(-50%);
    -ms-transform: translateY(-50%);
    right: 12px;
    color: #a0a0a0
}

.Popup_textGray200__d_ukK {
    color: #d4d4d4
}

.Popup_borderGray900__ExMNH {
    border-color: #2e2e2e
}

.Popup_modalBackground__cIWBi {
    position: fixed;
    inset: 0;
    margin: auto;
    background-color: rgba(0,0,0,.75);
    z-index: 8999
}

.Popup_popup__5pSbd {
    position: fixed;
    inset: 0;
    margin: auto;
    z-index: 9000;
    pointer-events: none
}

.Popup_popup__5pSbd .Popup_card__2Kp8X {
    position: fixed;
    inset: 0;
    margin: auto;
    display: flex;
    flex-direction: column;
    width: calc(100% - 32px);
    height: -moz-max-content;
    height: max-content;
    max-height: 80vh;
    background-color: #232323;
    border: 1px solid #2e2e2e;
    border-radius: 12px;
    pointer-events: all;
    overflow: hidden
}

@media screen and (min-width: 1024px) {
    .Popup_popup__5pSbd .Popup_card__2Kp8X {
        width:528px
    }
}

.Popup_popup__5pSbd .Popup_popupHeader__JVAAa {
    flex-shrink: 0;
    position: sticky;
    top: 0;
    left: 0;
    display: flex;
    align-items: center;
    justify-content: space-between;
    width: 100%;
    height: 56px;
    padding: 0 16px;
    border-bottom: 1px solid #2e2e2e
}

@media screen and (min-width: 1024px) {
    .Popup_popup__5pSbd .Popup_popupHeader__JVAAa {
        height:64px;
        padding: 0 24px
    }
}

.Popup_popup__5pSbd .Popup_popupHeader__JVAAa .Popup_popupTitle__OxHrr {
    font-size: 16px;
    line-height: 24px;
    font-weight: 700
}

@media screen and (min-width: 1024px) {
    .Popup_popup__5pSbd .Popup_popupHeader__JVAAa .Popup_popupTitle__OxHrr {
        font-size:20px;
        line-height: 28px
    }
}

.Popup_popup__5pSbd .Popup_popupContainer__wezcV {
    flex: 1;
    overflow-y: auto;
    padding: 16px;
    display: block
}

@media screen and (min-width: 1024px) {
    .Popup_popup__5pSbd .Popup_popupContainer__wezcV {
        padding:24px
    }
}

.Snackbar_textGray200___16Fo {
    color: #d4d4d4
}

.Snackbar_borderGray900__aWclU {
    border-color: #2e2e2e
}

.Snackbar_snackbarContainer__JE_uZ {
    position: fixed;
    bottom: 64px;
    right: 16px;
    width: calc(100% - 32px);
    max-width: 400px;
    display: flex;
    flex-direction: column;
    gap: 8px;
    z-index: 9999
}

@media screen and (min-width: 1024px) {
    .Snackbar_snackbarContainer__JE_uZ {
        bottom:32px;
        right: 32px
    }
}

.Snackbar_snackbarContainer__JE_uZ>div {
    display: flex;
    flex-direction: column;
    gap: 8px
}

.Snackbar_snackbar__gbNG6 {
    position: relative;
    width: 100%;
    padding: 12px;
    border-radius: 12px;
    color: #fff;
    font-size: 14px;
    background-color: rgba(62,62,62,.8);
    backdrop-filter: blur(160px);
    -webkit-backdrop-filter: blur(160px);
    border: 1px solid hsla(0,0%,100%,.05);
    box-shadow: 0 2px 12px rgba(0,0,0,.5)
}

.Snackbar_snackbar__gbNG6 .Snackbar_messageBox__3fWuu {
    display: flex;
    align-items: flex-start;
    gap: 8px;
    width: calc(100% - 32px)
}

.Snackbar_snackbar__gbNG6 .Snackbar_messageBox__3fWuu .Snackbar_message__I_6r2 {
    width: calc(100% - 20px)
}

.Snackbar_snackbar__gbNG6 .Snackbar_closeButtonBox__L65f2 {
    position: absolute;
    top: 6px;
    right: 6px
}

.Snackbar_loaderBox__dgXlD {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 20px;
    height: 20px
}

.Snackbar_loaderBox__dgXlD .Snackbar_loader__VqKIG {
    width: 16px;
    height: 16px;
    border: 2px solid #d4d4d4;
    border-bottom-color: transparent;
    border-radius: 50%;
    display: inline-block;
    box-sizing: border-box;
    animation: Snackbar_rotation__LOIqA 1s linear infinite
}

@keyframes Snackbar_rotation__LOIqA {
    0% {
        transform: rotate(0deg)
    }

    to {
        transform: rotate(1turn)
    }
}

.Snackbar_snackbarEnter__PpjEE {
    opacity: 0;
    transform: translateY(10px)
}

.Snackbar_snackbarEnterActive__IwdCq {
    opacity: 1;
    transform: translateY(0);
    transition: opacity .2s ease-in-out,transform .2s ease-in-out
}

.Snackbar_snackbarExit__4LW0v {
    opacity: 1;
    transform: translateY(0)
}

.Snackbar_snackbarExitActive__Ixo6P {
    opacity: 0;
    transform: translateY(10px);
    transition: opacity .2s ease-in-out,transform .2s ease-in-out
}

.Toolbar_textGray200__Rl1gb {
    color: #d4d4d4
}

.Toolbar_borderGray900__6k_Em {
    border-color: #2e2e2e
}

.Toolbar_normalToolbarWrapper__mbwtn {
    display: none
}

@media screen and (min-width: 1024px) {
    .Toolbar_normalToolbarWrapper__mbwtn {
        position:fixed;
        bottom: -96px;
        right: 0;
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 16px;
        width: calc(100% - 328px);
        z-index: 999;
        opacity: 0;
        transition: .2s ease-in
    }
}

.Toolbar_normalToolbarWrapper__mbwtn .Toolbar_toolbar__Az1jj {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 16px;
    width: 560px;
    padding: 8px;
    border-radius: 50px;
    background-color: #000;
    border: 1px solid #2e2e2e;
    box-shadow: 0 8px 32px rgba(0,0,0,.25);
    z-index: 999
}

.Toolbar_normalToolbarWrapper__mbwtn .Toolbar_toolbar__Az1jj .Toolbar_leftSection__rtF4L {
    display: flex;
    align-items: center;
    gap: 8px
}

.Toolbar_normalToolbarWrapper__mbwtn .Toolbar_toolbar__Az1jj .Toolbar_leftSection__rtF4L .Toolbar_currentSituation__vZSEW {
    font-size: 14px;
    line-height: 20px;
    color: #fff
}

.Toolbar_normalToolbarWrapper__mbwtn .Toolbar_toolbar__Az1jj .Toolbar_rightSection__kA1aC {
    display: flex;
    align-items: center;
    gap: 8px
}

.Toolbar_normalToolbarWrapper__mbwtn .Toolbar_toolbar__Az1jj .Toolbar_rightSection__kA1aC .Toolbar_dropdownButton__Qtb_U {
    font-weight: 700
}

.Toolbar_normalToolbarWrapper__mbwtn .Toolbar_toolbar__Az1jj .Toolbar_rightSection__kA1aC .Toolbar_dropdownButton__Qtb_U .Toolbar_proLabel__CuihL {
    position: relative;
    font-size: 12px;
    line-height: 16px;
    padding: 2px 8px;
    border-radius: 50px;
    background-color: #fff;
    color: #161616
}

.Toolbar_normalToolbarWrapper__mbwtn .Toolbar_toolbar__Az1jj .Toolbar_rightSection__kA1aC .Toolbar_dropdownButton__Qtb_U .Toolbar_proLabel__CuihL:before {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    border-radius: 50px;
    border: 2px solid transparent;
    background-image: linear-gradient(135deg,#f957dc,#b780ed 50%,#74a9ff);
    background-origin: border-box;
    background-clip: border-box;
    -webkit-mask-image: linear-gradient(#fff 0 0),linear-gradient(#fff 0 0);
    -webkit-mask-clip: padding-box,border-box;
    -webkit-mask-composite: destination-out;
    mask-image: linear-gradient(#fff 0 0),linear-gradient(#fff 0 0);
    mask-clip: padding-box,border-box;
    -webkit-mask-composite: xor;
    mask-composite: exclude
}

.Toolbar_searchPageToolbarWrapper__p6Qr3 {
    display: none
}

@media screen and (min-width: 1024px) {
    .Toolbar_searchPageToolbarWrapper__p6Qr3 {
        position:fixed;
        bottom: -96px;
        right: 0;
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 16px;
        width: calc(100% - 56px);
        z-index: 999;
        opacity: 0;
        transition: .2s ease-in
    }
}

.Toolbar_searchPageToolbarWrapper__p6Qr3 .Toolbar_toolbar__Az1jj {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 16px;
    width: 560px;
    padding: 8px;
    border-radius: 50px;
    background-color: #000;
    border: 1px solid #2e2e2e;
    box-shadow: 0 8px 32px rgba(0,0,0,.25);
    z-index: 999
}

.Toolbar_searchPageToolbarWrapper__p6Qr3 .Toolbar_toolbar__Az1jj .Toolbar_leftSection__rtF4L {
    display: flex;
    align-items: center;
    gap: 8px
}

.Toolbar_searchPageToolbarWrapper__p6Qr3 .Toolbar_toolbar__Az1jj .Toolbar_leftSection__rtF4L .Toolbar_currentSituation__vZSEW {
    font-size: 14px;
    line-height: 20px;
    color: #fff
}

.Toolbar_searchPageToolbarWrapper__p6Qr3 .Toolbar_toolbar__Az1jj .Toolbar_rightSection__kA1aC {
    display: flex;
    align-items: center;
    gap: 8px
}

.Toolbar_searchPageToolbarWrapper__p6Qr3 .Toolbar_toolbar__Az1jj .Toolbar_rightSection__kA1aC .Toolbar_dropdownButton__Qtb_U {
    font-weight: 700
}

.Toolbar_searchPageToolbarWrapper__p6Qr3 .Toolbar_toolbar__Az1jj .Toolbar_rightSection__kA1aC .Toolbar_dropdownButton__Qtb_U .Toolbar_proLabel__CuihL {
    position: relative;
    font-size: 12px;
    line-height: 16px;
    padding: 2px 8px;
    border-radius: 50px;
    background-color: #fff;
    color: #161616
}

.Toolbar_searchPageToolbarWrapper__p6Qr3 .Toolbar_toolbar__Az1jj .Toolbar_rightSection__kA1aC .Toolbar_dropdownButton__Qtb_U .Toolbar_proLabel__CuihL:before {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    border-radius: 50px;
    border: 2px solid transparent;
    background-image: linear-gradient(135deg,#f957dc,#b780ed 50%,#74a9ff);
    background-origin: border-box;
    background-clip: border-box;
    -webkit-mask-image: linear-gradient(#fff 0 0),linear-gradient(#fff 0 0);
    -webkit-mask-clip: padding-box,border-box;
    -webkit-mask-composite: destination-out;
    mask-image: linear-gradient(#fff 0 0),linear-gradient(#fff 0 0);
    mask-clip: padding-box,border-box;
    -webkit-mask-composite: xor;
    mask-composite: exclude
}

.Toolbar_toolbarWrapperActive__kCm_7 {
    bottom: 16px;
    opacity: 1;
    transition: all .2s ease-out
}
