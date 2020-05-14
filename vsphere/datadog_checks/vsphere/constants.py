# (C) Datadog, Inc. 2019-present
# All rights reserved
# Licensed under Simplified BSD License (see LICENSE)
from pyVmomi import vim

ALLOWED_FILTER_TYPES = ['whitelist', 'blacklist']
ALLOWED_FILTER_PROPERTIES = ['name', 'inventory_path', 'tag']
EXTRA_FILTER_PROPERTIES_FOR_VMS = ['hostname', 'guest_hostname']


SHORT_ROLLUP = {
    "average": "avg",
    "summation": "sum",
    "maximum": "max",
    "minimum": "min",
    "latest": "latest",
    "none": "raw",
}

MOR_TYPE_AS_STRING = {
    vim.HostSystem: 'host',
    vim.VirtualMachine: 'vm',
    vim.Datacenter: 'datacenter',
    vim.Datastore: 'datastore',
    vim.ClusterComputeResource: 'cluster',
}

ALL_RESOURCES = [
    vim.VirtualMachine,
    vim.HostSystem,
    vim.Datacenter,
    vim.Datastore,
    vim.ClusterComputeResource,
    vim.ComputeResource,
    vim.Folder,
]
REALTIME_RESOURCES = [vim.VirtualMachine, vim.HostSystem]
HISTORICAL_RESOURCES = [vim.Datacenter, vim.Datastore, vim.ClusterComputeResource]
ALL_RESOURCES_WITH_METRICS = REALTIME_RESOURCES + HISTORICAL_RESOURCES

REALTIME_METRICS_INTERVAL_ID = 20

DEFAULT_BATCH_COLLECTOR_SIZE = 500
DEFAULT_TAGS_COLLECTOR_SIZE = 200
DEFAULT_METRICS_PER_QUERY = 500
UNLIMITED_HIST_METRICS_PER_QUERY = float('inf')
DEFAULT_MAX_QUERY_METRICS = 256  # type: float
MAX_QUERY_METRICS_OPTION = "config.vpxd.stats.maxQueryMetrics"
DEFAULT_THREAD_COUNT = 4

DEFAULT_REFRESH_METRICS_METADATA_CACHE_INTERVAL = 1800
DEFAULT_REFRESH_INFRASTRUCTURE_CACHE_INTERVAL = 300

REFERENCE_METRIC = "cpu.usage.avg"

DEFAULT_VSPHERE_TAG_PREFIX = ""

ALLOWED_EVENTS = [
    vim.event.Event,
    vim.event.GeneralEvent,
    vim.event.GeneralHostInfoEvent,
    vim.event.GeneralHostWarningEvent,
    vim.event.GeneralHostErrorEvent,
    vim.event.GeneralVmInfoEvent,
    vim.event.GeneralVmWarningEvent,
    vim.event.GeneralVmErrorEvent,
    vim.event.GeneralUserEvent,
    vim.event.ExtendedEvent,
    vim.event.ExtendedEvent,
    vim.event.HealthStatusChangedEvent,
    vim.event.HostInventoryUnreadableEvent,
    vim.event.DatacenterEvent,
    vim.event.DatacenterCreatedEvent,
    vim.event.DatacenterRenamedEvent,
    vim.event.SessionEvent,
    vim.event.ServerStartedSessionEvent,
    vim.event.UserLoginSessionEvent,
    vim.event.UserLogoutSessionEvent,
    vim.event.BadUsernameSessionEvent,
    vim.event.AlreadyAuthenticatedSessionEvent,
    vim.event.NoAccessUserEvent,
    vim.event.SessionTerminatedEvent,
    vim.event.GlobalMessageChangedEvent,
    vim.event.UpgradeEvent,
    vim.event.InfoUpgradeEvent,
    vim.event.WarningUpgradeEvent,
    vim.event.ErrorUpgradeEvent,
    vim.event.UserUpgradeEvent,
    vim.event.HostEvent,
    vim.event.HostDasEvent,
    vim.event.HostConnectedEvent,
    vim.event.HostDisconnectedEvent,
    vim.event.HostSyncFailedEvent,
    vim.event.HostConnectionLostEvent,
    vim.event.HostReconnectionFailedEvent,
    vim.event.HostCnxFailedNoConnectionEvent,
    vim.event.HostCnxFailedBadUsernameEvent,
    vim.event.HostCnxFailedBadVersionEvent,
    vim.event.HostCnxFailedAlreadyManagedEvent,
    vim.event.HostCnxFailedNoLicenseEvent,
    vim.event.HostCnxFailedNetworkErrorEvent,
    vim.event.HostRemovedEvent,
    vim.event.HostCnxFailedCcagentUpgradeEvent,
    vim.event.HostCnxFailedBadCcagentEvent,
    vim.event.HostCnxFailedEvent,
    vim.event.HostCnxFailedAccountFailedEvent,
    vim.event.HostCnxFailedNoAccessEvent,
    vim.event.HostShutdownEvent,
    vim.event.HostCnxFailedNotFoundEvent,
    vim.event.HostCnxFailedTimeoutEvent,
    vim.event.HostUpgradeFailedEvent,
    vim.event.EnteringMaintenanceModeEvent,
    vim.event.EnteredMaintenanceModeEvent,
    vim.event.ExitMaintenanceModeEvent,
    vim.event.CanceledHostOperationEvent,
    vim.event.TimedOutHostOperationEvent,
    vim.event.HostDasEnabledEvent,
    vim.event.HostDasDisabledEvent,
    vim.event.HostDasEnablingEvent,
    vim.event.HostDasDisablingEvent,
    vim.event.HostDasErrorEvent,
    vim.event.HostDasOkEvent,
    vim.event.VcAgentUpgradedEvent,
    vim.event.VcAgentUninstalledEvent,
    vim.event.VcAgentUpgradeFailedEvent,
    vim.event.VcAgentUninstallFailedEvent,
    vim.event.HostAddedEvent,
    vim.event.HostAddFailedEvent,
    vim.event.HostIpChangedEvent,
    vim.event.EnteringStandbyModeEvent,
    vim.event.DrsEnteringStandbyModeEvent,
    vim.event.EnteredStandbyModeEvent,
    vim.event.DrsEnteredStandbyModeEvent,
    vim.event.ExitingStandbyModeEvent,
    vim.event.DrsExitingStandbyModeEvent,
    vim.event.ExitedStandbyModeEvent,
    vim.event.DrsExitedStandbyModeEvent,
    vim.event.ExitStandbyModeFailedEvent,
    vim.event.DrsExitStandbyModeFailedEvent,
    vim.event.UpdatedAgentBeingRestartedEvent,
    vim.event.AccountRemovedEvent,
    vim.event.UserPasswordChanged,
    vim.event.UserAssignedToGroup,
    vim.event.UserUnassignedFromGroup,
    vim.event.DatastorePrincipalConfigured,
    vim.event.VMFSDatastoreCreatedEvent,
    vim.event.NASDatastoreCreatedEvent,
    vim.event.LocalDatastoreCreatedEvent,
    vim.event.VMFSDatastoreExtendedEvent,
    vim.event.VMFSDatastoreExpandedEvent,
    vim.event.DatastoreRemovedOnHostEvent,
    vim.event.DatastoreRenamedOnHostEvent,
    vim.event.DuplicateIpDetectedEvent,
    vim.event.DatastoreDiscoveredEvent,
    vim.event.DrsResourceConfigureFailedEvent,
    vim.event.DrsResourceConfigureSyncedEvent,
    vim.event.HostGetShortNameFailedEvent,
    vim.event.HostShortNameToIpFailedEvent,
    vim.event.HostIpToShortNameFailedEvent,
    vim.event.HostPrimaryAgentNotShortNameEvent,
    vim.event.HostNotInClusterEvent,
    vim.event.HostIsolationIpPingFailedEvent,
    vim.event.HostIpInconsistentEvent,
    vim.event.HostUserWorldSwapNotEnabledEvent,
    vim.event.HostNonCompliantEvent,
    vim.event.HostCompliantEvent,
    vim.event.HostComplianceCheckedEvent,
    vim.event.ProfileEvent,
    vim.event.ProfileCreatedEvent,
    vim.event.ProfileRemovedEvent,
    vim.event.ProfileAssociatedEvent,
    vim.event.ProfileDissociatedEvent,
    vim.event.HostConfigAppliedEvent,
    vim.event.ProfileReferenceHostChangedEvent,
    vim.event.ProfileChangedEvent,
    vim.event.HostProfileAppliedEvent,
    vim.event.HostShortNameInconsistentEvent,
    vim.event.HostNoRedundantManagementNetworkEvent,
    vim.event.HostNoAvailableNetworksEvent,
    vim.event.HostExtraNetworksEvent,
    vim.event.HostNoHAEnabledPortGroupsEvent,
    vim.event.HostMissingNetworksEvent,
    vim.event.VnicPortArgument,
    vim.event.HostVnicConnectedToCustomizedDVPortEvent,
    vim.event.GhostDvsProxySwitchDetectedEvent,
    vim.event.GhostDvsProxySwitchRemovedEvent,
    vim.event.VmEvent,
    vim.event.VmPoweredOffEvent,
    vim.event.VmPoweredOnEvent,
    vim.event.VmSuspendedEvent,
    vim.event.VmStartingEvent,
    vim.event.VmStoppingEvent,
    vim.event.VmSuspendingEvent,
    vim.event.VmResumingEvent,
    vim.event.VmDisconnectedEvent,
    vim.event.VmRemoteConsoleConnectedEvent,
    vim.event.VmRemoteConsoleDisconnectedEvent,
    vim.event.VmDiscoveredEvent,
    vim.event.VmOrphanedEvent,
    vim.event.VmBeingCreatedEvent,
    vim.event.VmCreatedEvent,
    vim.event.VmStartRecordingEvent,
    vim.event.VmEndRecordingEvent,
    vim.event.VmStartReplayingEvent,
    vim.event.VmEndReplayingEvent,
    vim.event.VmRegisteredEvent,
    vim.event.VmAutoRenameEvent,
    vim.event.VmBeingHotMigratedEvent,
    vim.event.VmResettingEvent,
    vim.event.VmStaticMacConflictEvent,
    vim.event.VmMacConflictEvent,
    vim.event.VmBeingDeployedEvent,
    vim.event.VmDeployFailedEvent,
    vim.event.VmDeployedEvent,
    vim.event.VmMacChangedEvent,
    vim.event.VmMacAssignedEvent,
    vim.event.VmUuidConflictEvent,
    vim.event.VmInstanceUuidConflictEvent,
    vim.event.VmBeingMigratedEvent,
    vim.event.VmFailedMigrateEvent,
    vim.event.VmMigratedEvent,
    vim.event.VmUnsupportedStartingEvent,
    vim.event.DrsVmMigratedEvent,
    vim.event.DrsVmPoweredOnEvent,
    vim.event.DrsRuleViolationEvent,
    vim.event.DrsSoftRuleViolationEvent,
    vim.event.DrsRuleComplianceEvent,
    vim.event.VmRelocateSpecEvent,
    vim.event.VmBeingRelocatedEvent,
    vim.event.VmRelocatedEvent,
    vim.event.VmRelocateFailedEvent,
    vim.event.VmEmigratingEvent,
    vim.event.VmCloneEvent,
    vim.event.VmBeingClonedEvent,
    vim.event.VmBeingClonedNoFolderEvent,
    vim.event.VmCloneFailedEvent,
    vim.event.VmClonedEvent,
    vim.event.VmResourceReallocatedEvent,
    vim.event.VmRenamedEvent,
    vim.event.VmDateRolledBackEvent,
    vim.event.VmNoNetworkAccessEvent,
    vim.event.VmDiskFailedEvent,
    vim.event.VmFailedToPowerOnEvent,
    vim.event.VmFailedToPowerOffEvent,
    vim.event.VmFailedToSuspendEvent,
    vim.event.VmFailedToResetEvent,
    vim.event.VmFailedToShutdownGuestEvent,
    vim.event.VmFailedToRebootGuestEvent,
    vim.event.VmFailedToStandbyGuestEvent,
    vim.event.VmRemovedEvent,
    vim.event.VmGuestShutdownEvent,
    vim.event.VmGuestRebootEvent,
    vim.event.VmGuestStandbyEvent,
    vim.event.VmUpgradingEvent,
    vim.event.VmUpgradeCompleteEvent,
    vim.event.VmUpgradeFailedEvent,
    vim.event.VmRestartedOnAlternateHostEvent,
    vim.event.VmReconfiguredEvent,
    vim.event.VmMessageEvent,
    vim.event.VmMessageWarningEvent,
    vim.event.VmMessageErrorEvent,
    vim.event.VmConfigMissingEvent,
    vim.event.VmPowerOffOnIsolationEvent,
    vim.event.VmShutdownOnIsolationEvent,
    vim.event.VmFailoverFailed,
    vim.event.VmDasBeingResetEvent,
    vim.event.VmDasResetFailedEvent,
    vim.event.VmMaxRestartCountReached,
    vim.event.VmMaxFTRestartCountReached,
    vim.event.VmDasBeingResetWithScreenshotEvent,
    vim.event.NotEnoughResourcesToStartVmEvent,
    vim.event.VmUuidAssignedEvent,
    vim.event.VmInstanceUuidAssignedEvent,
    vim.event.VmUuidChangedEvent,
    vim.event.VmInstanceUuidChangedEvent,
    vim.event.VmWwnConflictEvent,
    vim.event.VmAcquiredMksTicketEvent,
    vim.event.VmAcquiredTicketEvent,
    vim.event.VmGuestOSCrashedEvent,
    vim.event.HostWwnConflictEvent,
    vim.event.VmWwnAssignedEvent,
    vim.event.VmWwnChangedEvent,
    vim.event.VmSecondaryAddedEvent,
    vim.event.VmFaultToleranceTurnedOffEvent,
    vim.event.VmSecondaryDisabledEvent,
    vim.event.VmSecondaryDisabledBySystemEvent,
    vim.event.VmSecondaryEnabledEvent,
    vim.event.VmStartingSecondaryEvent,
    vim.event.VmSecondaryStartedEvent,
    vim.event.VmFailedUpdatingSecondaryConfig,
    vim.event.VmFailedStartingSecondaryEvent,
    vim.event.VmTimedoutStartingSecondaryEvent,
    vim.event.VmNoCompatibleHostForSecondaryEvent,
    vim.event.VmPrimaryFailoverEvent,
    vim.event.VmFaultToleranceVmTerminatedEvent,
    vim.event.HostWwnChangedEvent,
    vim.event.HostAdminDisableEvent,
    vim.event.HostAdminEnableEvent,
    vim.event.VmFailedRelayoutOnVmfs2DatastoreEvent,
    vim.event.VmFailedRelayoutEvent,
    vim.event.VmRelayoutSuccessfulEvent,
    vim.event.VmRelayoutUpToDateEvent,
    vim.event.VmConnectedEvent,
    vim.event.VmPoweringOnWithCustomizedDVPortEvent,
    vim.event.VmDasUpdateErrorEvent,
    vim.event.NoMaintenanceModeDrsRecommendationForVM,
    vim.event.VmDasUpdateOkEvent,
    vim.event.ScheduledTaskEvent,
    vim.event.ScheduledTaskCreatedEvent,
    vim.event.ScheduledTaskStartedEvent,
    vim.event.ScheduledTaskRemovedEvent,
    vim.event.ScheduledTaskReconfiguredEvent,
    vim.event.ScheduledTaskCompletedEvent,
    vim.event.ScheduledTaskFailedEvent,
    vim.event.ScheduledTaskEmailCompletedEvent,
    vim.event.ScheduledTaskEmailFailedEvent,
    vim.event.AlarmEvent,
    vim.event.AlarmCreatedEvent,
    vim.event.AlarmStatusChangedEvent,
    vim.event.AlarmActionTriggeredEvent,
    vim.event.AlarmEmailCompletedEvent,
    vim.event.AlarmEmailFailedEvent,
    vim.event.AlarmSnmpCompletedEvent,
    vim.event.AlarmSnmpFailedEvent,
    vim.event.AlarmScriptCompleteEvent,
    vim.event.AlarmScriptFailedEvent,
    vim.event.AlarmRemovedEvent,
    vim.event.AlarmReconfiguredEvent,
    vim.event.AlarmAcknowledgedEvent,
    vim.event.AlarmClearedEvent,
    vim.event.CustomFieldEvent,
    vim.event.CustomFieldDefEvent,
    vim.event.CustomFieldDefAddedEvent,
    vim.event.CustomFieldDefRemovedEvent,
    vim.event.CustomFieldDefRenamedEvent,
    vim.event.CustomFieldValueChangedEvent,
    vim.event.AuthorizationEvent,
    vim.event.PermissionEvent,
    vim.event.PermissionAddedEvent,
    vim.event.PermissionUpdatedEvent,
    vim.event.PermissionRemovedEvent,
    vim.event.RoleEvent,
    vim.event.RoleAddedEvent,
    vim.event.RoleUpdatedEvent,
    vim.event.RoleRemovedEvent,
    vim.event.DatastoreEvent,
    vim.event.DatastoreDestroyedEvent,
    vim.event.DatastoreRenamedEvent,
    vim.event.DatastoreCapacityIncreasedEvent,
    vim.event.DatastoreDuplicatedEvent,
    vim.event.DatastoreFileEvent,
    vim.event.DatastoreFileCopiedEvent,
    vim.event.DatastoreFileMovedEvent,
    vim.event.DatastoreFileDeletedEvent,
    vim.event.NonVIWorkloadDetectedOnDatastoreEvent,
    vim.event.DatastoreIORMReconfiguredEvent,
    vim.event.TaskEvent,
    vim.event.TaskTimeoutEvent,
    vim.event.LicenseEvent,
    vim.event.ServerLicenseExpiredEvent,
    vim.event.HostLicenseExpiredEvent,
    vim.event.VMotionLicenseExpiredEvent,
    vim.event.NoLicenseEvent,
    vim.event.LicenseServerUnavailableEvent,
    vim.event.LicenseServerAvailableEvent,
    vim.event.LicenseExpiredEvent,
    vim.event.InvalidEditionEvent,
    vim.event.HostInventoryFullEvent,
    vim.event.LicenseRestrictedEvent,
    vim.event.IncorrectHostInformationEvent,
    vim.event.UnlicensedVirtualMachinesEvent,
    vim.event.UnlicensedVirtualMachinesFoundEvent,
    vim.event.AllVirtualMachinesLicensedEvent,
    vim.event.LicenseNonComplianceEvent,
    vim.event.MigrationEvent,
    vim.event.MigrationWarningEvent,
    vim.event.MigrationErrorEvent,
    vim.event.MigrationHostWarningEvent,
    vim.event.MigrationHostErrorEvent,
    vim.event.MigrationResourceWarningEvent,
    vim.event.MigrationResourceErrorEvent,
    vim.event.ClusterEvent,
    vim.event.DasEnabledEvent,
    vim.event.DasDisabledEvent,
    vim.event.DasAdmissionControlDisabledEvent,
    vim.event.DasAdmissionControlEnabledEvent,
    vim.event.DasHostFailedEvent,
    vim.event.DasHostIsolatedEvent,
    vim.event.DasClusterIsolatedEvent,
    vim.event.DasAgentUnavailableEvent,
    vim.event.DasAgentFoundEvent,
    vim.event.InsufficientFailoverResourcesEvent,
    vim.event.FailoverLevelRestored,
    vim.event.ClusterOvercommittedEvent,
    vim.event.HostOvercommittedEvent,
    vim.event.ClusterStatusChangedEvent,
    vim.event.HostStatusChangedEvent,
    vim.event.ClusterCreatedEvent,
    vim.event.ClusterDestroyedEvent,
    vim.event.DrsEnabledEvent,
    vim.event.DrsDisabledEvent,
    vim.event.ClusterReconfiguredEvent,
    vim.event.HostMonitoringStateChangedEvent,
    vim.event.VmHealthMonitoringStateChangedEvent,
    vim.event.ResourcePoolEvent,
    vim.event.ResourcePoolCreatedEvent,
    vim.event.ResourcePoolDestroyedEvent,
    vim.event.ResourcePoolMovedEvent,
    vim.event.ResourcePoolReconfiguredEvent,
    vim.event.ResourceViolatedEvent,
    vim.event.VmResourcePoolMovedEvent,
    vim.event.TemplateUpgradeEvent,
    vim.event.TemplateBeingUpgradedEvent,
    vim.event.TemplateUpgradeFailedEvent,
    vim.event.TemplateUpgradedEvent,
    vim.event.CustomizationEvent,
    vim.event.CustomizationStartedEvent,
    vim.event.CustomizationSucceeded,
    vim.event.CustomizationFailed,
    vim.event.CustomizationUnknownFailure,
    vim.event.CustomizationSysprepFailed,
    vim.event.CustomizationLinuxIdentityFailed,
    vim.event.CustomizationNetworkSetupFailed,
    vim.event.LockerMisconfiguredEvent,
    vim.event.LockerReconfiguredEvent,
    vim.event.NoDatastoresConfiguredEvent,
    vim.event.AdminPasswordNotChangedEvent,
    vim.event.HostInAuditModeEvent,
    vim.event.LocalTSMEnabledEvent,
    vim.event.RemoteTSMEnabledEvent,
    vim.event.VimAccountPasswordChangedEvent,
    vim.event.iScsiBootFailureEvent,
    vim.event.DvsHealthStatusChangeEvent,
    vim.event.NetworkRollbackEvent,
    vim.event.UplinkPortVlanTrunkedEvent,
    vim.event.UplinkPortVlanUntrunkedEvent,
    vim.event.MtuMatchEvent,
    vim.event.MtuMismatchEvent,
    vim.event.UplinkPortMtuNotSupportEvent,
    vim.event.UplinkPortMtuSupportEvent,
    vim.event.TeamingMatchEvent,
    vim.event.TeamingMisMatchEvent,
    vim.event.DvsEvent,
    vim.event.DvsCreatedEvent,
    vim.event.DvsRenamedEvent,
    vim.event.DvsUpgradeAvailableEvent,
    vim.event.DvsUpgradeInProgressEvent,
    vim.event.DvsUpgradeRejectedEvent,
    vim.event.DvsUpgradedEvent,
    vim.event.DvsHostJoinedEvent,
    vim.event.DvsHostLeftEvent,
    vim.event.DvsOutOfSyncHostArgument,
    vim.event.OutOfSyncDvsHost,
    vim.event.DvsHostWentOutOfSyncEvent,
    vim.event.DvsHostBackInSyncEvent,
    vim.event.DvsHostStatusUpdated,
    vim.event.DvsPortCreatedEvent,
    vim.event.DvsPortReconfiguredEvent,
    vim.event.DvsPortDeletedEvent,
    vim.event.DvsPortConnectedEvent,
    vim.event.DvsPortDisconnectedEvent,
    vim.event.DvsPortVendorSpecificStateChangeEvent,
    vim.event.DvsPortRuntimeChangeEvent,
    vim.event.DvsPortLinkUpEvent,
    vim.event.DvsPortLinkDownEvent,
    vim.event.DvsPortJoinPortgroupEvent,
    vim.event.DvsPortLeavePortgroupEvent,
    vim.event.DvsPortBlockedEvent,
    vim.event.DvsPortUnblockedEvent,
    vim.event.DvsPortEnteredPassthruEvent,
    vim.event.DvsPortExitedPassthruEvent,
    vim.event.DvsDestroyedEvent,
    vim.event.DvsMergedEvent,
    vim.event.HostLocalPortCreatedEvent,
    vim.event.RollbackEvent,
    vim.event.RecoveryEvent,
    vim.event.DvsImportEvent,
    vim.event.DvsRestoreEvent,
    vim.event.VmVnicPoolReservationViolationRaiseEvent,
    vim.event.VmVnicPoolReservationViolationClearEvent,
    vim.event.DVPortgroupEvent,
    vim.event.DVPortgroupCreatedEvent,
    vim.event.DVPortgroupRenamedEvent,
    vim.event.DVPortgroupDestroyedEvent,
    vim.event.DvpgImportEvent,
    vim.event.DvpgRestoreEvent,
    vim.event.DrsInvocationFailedEvent,
    vim.event.DrsRecoveredFromFailureEvent,
    vim.event.VmReloadFromPathEvent,
    vim.event.VmReloadFromPathFailedEvent,
    vim.event.VmRequirementsExceedCurrentEVCModeEvent,
    vim.event.EventArgument,
    vim.event.RoleEventArgument,
    vim.event.EntityEventArgument,
    vim.event.ManagedEntityEventArgument,
    vim.event.FolderEventArgument,
    vim.event.DatacenterEventArgument,
    vim.event.ComputeResourceEventArgument,
    vim.event.ResourcePoolEventArgument,
    vim.event.HostEventArgument,
    vim.event.VmEventArgument,
    vim.event.DatastoreEventArgument,
    vim.event.NetworkEventArgument,
    vim.event.AlarmEventArgument,
    vim.event.ScheduledTaskEventArgument,
    vim.event.ProfileEventArgument,
    vim.event.DvsEventArgument,
    vim.event.ChangesInfoEventArgument,
    vim.event.EventDescription,
    vim.event.EventDescription,
    vim.event.EventDescription,
    vim.event.EventEx,
    vim.event.EventFilterSpec,
    vim.event.EventFilterSpec,
    vim.event.EventFilterSpec,
    vim.event.EventFilterSpec,
    vim.event.AccountCreatedEvent,
    vim.event.AccountUpdatedEvent,
    vim.event.ClusterComplianceCheckedEvent,
    vim.event.VmFaultToleranceStateChangedEvent,
    vim.event.HostEnableAdminFailedEvent,
    vim.event.DVPortgroupReconfiguredEvent,
    vim.event.DvsReconfiguredEvent,
]
