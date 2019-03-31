## The contents of this file are subject to the Common Public Attribution
## License Version 1.0. (the "License"); you may not use this file except in
## compliance with the License. You may obtain a copy of the License at
## http://code.reddit.com/LICENSE. The License is based on the Mozilla Public
## License Version 1.1, but Sections 14 and 15 have been added to cover use of
## software over a computer network and provide for limited attribution for the
## Original Developer. In addition, Exhibit A has been modified to be
## consistent with Exhibit B.
##
## Software distributed under the License is distributed on an "AS IS" basis,
## WITHOUT WARRANTY OF ANY KIND, either express or implied. See the License for
## the specific language governing rights and limitations under the License.
##
## The Original Code is reddit.
##
## The Original Developer is the Initial Developer.  The Initial Developer of
## the Original Code is reddit Inc.
##
## All portions of the code written by reddit are Copyright (c) 2006-2015
## reddit Inc. All Rights Reserved.
###############################################################################

<%!
  from r2.lib.filters import keep_space
%>

<%namespace file="printablebuttons.m" import="toggle_button" />
<%namespace file="usertext.m" import="markhelp" />

<div style="display: none;" id="wiki_edit_conflict">
    <h2 class="error">there was a conflict editing</h2>
    <h1>${_("your edit")}</h1>
    <em>${_("this edit is for you to resolve the conflict, any text in the box below will not save.")}</em><br/>
    <textarea id="youredit"></textarea>
    <span id="yourdiff"></span>
    <h1>${_("current edit")}</h1>
</div>

<div style="display: none;" id="wiki_special_error">
    <h1>Errors: </h1>
    <span id="specials" class="error"></span>
</div>

<form method="post" id="editform" onsubmit="r.wiki.submitEdit(event)">
    <textarea name="content" rows="20" cols="20" style="width: 97%" id="wiki_page_content">${keep_space(thing.page_content)}</textarea>
    ${toggle_button("help-toggle", _("formatting help"), _("hide help"), "r.wiki.helpon", "r.wiki.helpoff")}
    ${markhelp()}
    <br/><br/>
    <label for="reason">${_("reason for revision")}</label><br/>
    <input type="text" name="reason" maxlength="256" id="wiki_revision_reason" />
    <input type="hidden" id="previous" name="previous" value="${thing.previous}" />
    <br/><br/><input type="submit" id="wiki_save_button" class="wiki_button" value="${_('save page')}" />
    <span class="throbber" />
</form>
