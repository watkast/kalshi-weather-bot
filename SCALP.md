# Range-Scalp Bot

*Updated Sun Nov 22 10:52 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 68501 | 59769 | 8732 (142) | 4 | $-18447.56 | -4.3% |
| **+10¢** | 51153 | 40952 | 10201 (186) | 5 | $-17128.16 | -5.3% |
| **+15¢** | 42871 | 31877 | 10994 (237) | 7 | $-15356.15 | -5.7% |
| **+20¢** | 38167 | 26614 | 11553 (295) | 9 | $-13683.07 | -5.7% |
| **+10¢ (15¢ stop)** | 83447 | 83262 | 185 (116) | 4 | $-30705.88 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-22 10:51 | +10 stop | DOGE | UP | 0.56 | 0.32 | -2.74 |
| 11-22 10:51 | +5 | BNB | DOWN | 0.66 | open |  |
| 11-22 10:51 | +10 stop | XRP | UP | 0.70 | 0.07 | -6.53 |
| 11-22 10:51 | +20 | XRP | UP | 0.70 | open |  |
| 11-22 10:51 | +15 | XRP | UP | 0.70 | open |  |
| 11-22 10:51 | +5 | BTC | UP | 0.66 | 0.72 | 0.29 |
| 11-22 10:50 | +10 stop | DOGE | UP | 0.52 | 0.64 | 0.85 |
| 11-22 10:50 | +10 stop | ETH | DOWN | 0.60 | open |  |
| 11-22 10:50 | +10 stop | BNB | DOWN | 0.71 | open |  |
| 11-22 10:50 | +5 | BTC | UP | 0.61 | 0.67 | 0.27 |
| 11-22 10:50 | +10 stop | DOGE | UP | 0.49 | 0.61 | 0.85 |
| 11-22 10:49 | +10 stop | SOL | UP | 0.54 | open |  |
| 11-22 10:49 | +10 stop | BNB | UP | 0.59 | 0.37 | -2.54 |
| 11-22 10:49 | +5 | ETH | UP | 0.68 | open |  |
| 11-22 10:49 | +10 stop | ZEC | UP | 0.54 | 0.28 | -2.93 |
| 11-22 10:48 | +10 stop | SOL | UP | 0.60 | 0.71 | 0.78 |
| 11-22 10:48 | +10 stop | DOGE | UP | 0.61 | 0.71 | 0.68 |
| 11-22 10:48 | +5 | NEAR | UP | 0.64 | 0.69 | 0.18 |
| 11-22 10:48 | +10 stop | BNB | UP | 0.56 | 0.68 | 0.86 |
| 11-22 10:47 | +10 stop | ETH | UP | 0.60 | 0.45 | -1.85 |
| 11-22 10:47 | +20 | ETH | UP | 0.60 | open |  |
| 11-22 10:47 | +15 | ETH | UP | 0.60 | open |  |
| 11-22 10:47 | +10 | ETH | UP | 0.60 | open |  |
| 11-22 10:47 | +5 | ETH | UP | 0.60 | 0.67 | 0.37 |
| 11-22 10:47 | +15 | BTC | UP | 0.71 | open |  |
| 11-22 10:47 | +10 | BTC | UP | 0.71 | open |  |
| 11-22 10:47 | +5 | BTC | UP | 0.71 | 0.76 | 0.22 |
| 11-22 10:47 | +10 stop | BTC | UP | 0.70 | open |  |
| 11-22 10:47 | +20 | BTC | UP | 0.71 | open |  |
| 11-22 10:47 | +10 stop | NEAR | UP | 0.66 | 0.85 | 1.65 |
| 11-22 10:47 | +20 | NEAR | UP | 0.66 | open |  |
| 11-22 10:47 | +15 | NEAR | UP | 0.65 | 0.85 | 1.75 |
| 11-22 10:47 | +10 | NEAR | UP | 0.63 | 0.73 | 0.69 |
| 11-22 10:47 | +5 | NEAR | UP | 0.57 | 0.68 | 0.76 |
| 11-22 10:47 | +10 stop | DOGE | DOWN | 0.51 | 0.35 | -1.94 |
| 11-22 10:47 | +20 | DOGE | DOWN | 0.51 | open |  |
| 11-22 10:47 | +15 | DOGE | DOWN | 0.51 | 0.66 | 1.16 |
| 11-22 10:47 | +10 | DOGE | DOWN | 0.51 | 0.66 | 1.16 |
| 11-22 10:47 | +5 | DOGE | DOWN | 0.51 | 0.66 | 1.16 |
| 11-22 10:46 | +10 stop | SOL | DOWN | 0.56 | 0.36 | -2.35 |
