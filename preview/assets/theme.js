(function () {
  "use strict";

  var H1 = {
    cooling: "No cooling? We’ll send a GTA tech.",
    heat: "No heat? Call a Markham dispatch team.",
    condo: "Condo blowing warm air? Fan coils and heat pumps.",
    commercial: "Rooftop down? Commercial HVAC for GTA plazas.",
    install: "New furnace, AC, or heat pump — get a quote.",
    maintenance: "Maintenance before the next no-heat night.",
    default: "GTA HVAC repair and install — houses, condos, and rooftops."
  };

  var JOB_FROM_PARAM = {
    cooling: "No cooling",
    nocooling: "No cooling",
    ac: "No cooling",
    heat: "No heat",
    noheat: "No heat",
    furnace: "No heat",
    condo: "Condo fan coil / heat pump",
    fancoil: "Condo fan coil / heat pump",
    wshp: "Condo fan coil / heat pump",
    commercial: "Commercial rooftop",
    rtu: "Commercial rooftop",
    rooftop: "Commercial rooftop",
    install: "New install / quote",
    quote: "New install / quote",
    maintenance: "Maintenance",
    tuneup: "Maintenance"
  };

  var PRODUCT_TO_JOB = {
    "furnace": "New install / quote",
    "ac": "New install / quote",
    "heat-pump": "New install / quote",
    "ductless": "New install / quote",
    "boiler": "New install / quote",
    "fan-coil": "Condo fan coil / heat pump",
    "vfc": "Condo fan coil / heat pump",
    "wshp": "Condo fan coil / heat pump",
    "magic-pak": "Condo fan coil / heat pump",
    "ptac": "Condo fan coil / heat pump",
    "rtu": "Commercial rooftop",
    "mau": "Commercial rooftop",
    "ventilation": "Commercial rooftop"
  };

  function qs(sel, root) { return (root || document).querySelector(sel); }
  function qsa(sel, root) { return Array.prototype.slice.call((root || document).querySelectorAll(sel)); }
  function param(name) {
    try { return new URLSearchParams(window.location.search).get(name) || ""; }
    catch (e) { return ""; }
  }

  function setHero() {
    var el = qs("[data-hero-h1]");
    if (!el) return;
    var key = (param("job") || param("h1") || param("utm_content") || "").toLowerCase().replace(/\s+/g, "");
    var text = H1[key] || H1.default;
    el.textContent = text;
    var hidden = qs("[name='contact[h1_variant]'], [name='h1_variant']");
    if (hidden) hidden.value = text;
  }

  function fillHiddenCampaign() {
    var keys = ["utm_source", "utm_medium", "utm_campaign", "utm_content", "utm_term", "gclid", "wbraid", "gbraid", "msclkid"];
    keys.forEach(function (k) {
      var val = param(k);
      qsa("[name='contact[" + k + "]'], [name='" + k + "']").forEach(function (input) {
        if (val) input.value = val;
      });
    });
    qsa("[name='contact[landing_page]'], [name='landing_page']").forEach(function (input) {
      input.value = window.location.href;
    });
    var product = param("product");
    if (product) {
      qsa("[name='contact[product]'], [name='product']").forEach(function (input) {
        input.value = product;
      });
    }
  }

  function prefillPicker() {
    var jobKey = (param("job") || param("product") || "").toLowerCase();
    var job = JOB_FROM_PARAM[jobKey] || PRODUCT_TO_JOB[jobKey];
    if (job) {
      var radio = qs("input[name='job_type'][value='" + job + "']");
      if (radio) radio.checked = true;
    }
    var prop = param("property");
    if (prop) {
      var map = { house: "House", home: "House", condo: "Condo / high-rise", commercial: "Commercial" };
      var val = map[prop.toLowerCase()];
      if (val) {
        var pr = qs("input[name='property_type'][value='" + val + "']");
        if (pr) pr.checked = true;
      }
    }
    syncPickerToForm();
  }

  function syncPickerToForm() {
    var job = qs("input[name='job_type']:checked");
    var prop = qs("input[name='property_type']:checked");
    var city = qs("[data-city-input]");
    var jobField = qs("[data-job-field]");
    var propField = qs("[data-property-field]");
    var cityField = qs("[data-city-field]");
    if (job && jobField) jobField.value = job.value;
    if (prop && propField) propField.value = prop.value;
    if (city && cityField) cityField.value = city.value;
  }

  function bindPicker() {
    qsa("input[name='job_type'], input[name='property_type']").forEach(function (el) {
      el.addEventListener("change", syncPickerToForm);
    });
    var city = qs("[data-city-input]");
    if (city) city.addEventListener("input", syncPickerToForm);
  }

  function bindMenu() {
    var btn = qs("[data-menu-toggle]");
    var panel = qs("[data-nav-panel]");
    if (!btn || !panel) return;
    btn.addEventListener("click", function () {
      var open = btn.getAttribute("aria-expanded") === "true";
      btn.setAttribute("aria-expanded", open ? "false" : "true");
      panel.hidden = open;
    });
  }

  function canadianPhone(value) {
    var digits = (value || "").replace(/\D/g, "");
    if (digits.length === 11 && digits.charAt(0) === "1") digits = digits.slice(1);
    return digits.length === 10;
  }

  function bindForm() {
    var form = qs("[data-job-form]");
    if (!form) return;
    form.setAttribute("novalidate", "");
    form.addEventListener("submit", function (e) {
      syncPickerToForm();
      var status = qs("[data-form-status]", form);
      var name = qs("[name='contact[name]'], [name='name']", form);
      var mobile = qs("[name='contact[phone]'], [name='mobile']", form);
      var job = qs("[data-job-field]", form);
      var errors = [];
      if (!name || !name.value.trim()) errors.push("Add your name.");
      if (!mobile || !canadianPhone(mobile.value)) errors.push("Add a 10-digit Canadian mobile.");
      if (!job || !job.value.trim()) errors.push("Pick what you need — no cooling, no heat, condo, install, rooftop, or maintenance.");
      if (errors.length) {
        e.preventDefault();
        if (status) {
          status.hidden = false;
          status.textContent = errors.join(" ");
        }
        return;
      }
      var email = qs("[name='contact[email]'], [name='email']", form);
      if (email && !email.value.trim()) {
        email.value = "mobile-lead@servicexpress.ca";
      }
      var body = qs("[name='contact[body]'], [name='body']", form);
      if (body) {
        body.value = buildBody(form);
      }

      var endpoint = form.getAttribute("data-endpoint") || "";
      var thanks = form.getAttribute("data-thanks") || "/pages/thank-you";
      var isShopify = form.getAttribute("data-platform") === "shopify" && !endpoint;

      if (!isShopify) {
        e.preventDefault();
        var payload = collect(form);
        try { sessionStorage.setItem("sx_job", JSON.stringify(payload)); } catch (err) {}
        if (endpoint) {
          fetch(endpoint, {
            method: "POST",
            headers: { "Accept": "application/json", "Content-Type": "application/json" },
            body: JSON.stringify(payload)
          }).catch(function () {});
        }
        window.location.href = thanks;
      }
    });
  }

  function collect(form) {
    var data = {};
    qsa("input, select, textarea", form).forEach(function (el) {
      if (!el.name || el.type === "file") return;
      if ((el.type === "radio" || el.type === "checkbox") && !el.checked) return;
      data[el.name] = el.value;
    });
    var file = qs("input[type='file']", form);
    if (file && file.files && file.files[0]) data.photo_name = file.files[0].name;
    return data;
  }

  function buildBody(form) {
    var get = function (sel) {
      var el = qs(sel, form);
      return el ? el.value : "";
    };
    var emergency = qs("[name='contact[emergency_today]'], [name='emergency_today']", form);
    return [
      "Job request from servicexp.ca ads landing",
      "Name: " + get("[name='contact[name]'], [name='name']"),
      "Mobile: " + get("[name='contact[phone]'], [name='mobile']"),
      "Job type: " + get("[data-job-field]"),
      "Property: " + get("[data-property-field]"),
      "City / postal: " + get("[data-city-field]"),
      "Address / intersection: " + get("[name='contact[address]'], [name='address']"),
      "Emergency today: " + (emergency && emergency.checked ? "Yes" : "No"),
      "Product: " + get("[name='contact[product]'], [name='product']"),
      "Notes: " + get("[name='notes']"),
      "Page: " + window.location.href
    ].join("\n");
  }

  function bindThanks() {
    var box = qs("[data-thanks-number]");
    if (!box) return;
    try {
      var raw = sessionStorage.getItem("sx_job");
      if (!raw) return;
      var data = JSON.parse(raw);
      var phone = data["contact[phone]"] || data.mobile || "";
      if (phone) box.textContent = phone;
    } catch (e) {}
  }

  document.addEventListener("DOMContentLoaded", function () {
    setHero();
    fillHiddenCampaign();
    prefillPicker();
    bindPicker();
    bindMenu();
    bindForm();
    bindThanks();
  });
})();
