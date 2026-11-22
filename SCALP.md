# Range-Scalp Bot

*Updated Sun Nov 22 12:34 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 68633 | 59884 | 8749 (142) | 2 | $-18493.40 | -4.3% |
| **+10¢** | 51244 | 41025 | 10219 (186) | 2 | $-17155.37 | -5.3% |
| **+15¢** | 42948 | 31933 | 11015 (237) | 2 | $-15394.07 | -5.7% |
| **+20¢** | 38234 | 26660 | 11574 (295) | 2 | $-13713.91 | -5.7% |
| **+10¢ (15¢ stop)** | 83594 | 83409 | 185 (116) | 1 | $-30781.87 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-22 12:34 | +10 stop | BTC | UP | 0.65 | open |  |
| 11-22 12:34 | +20 | BTC | UP | 0.64 | open |  |
| 11-22 12:34 | +15 | BTC | UP | 0.63 | open |  |
| 11-22 12:34 | +10 | BTC | UP | 0.63 | open |  |
| 11-22 12:34 | +5 | BTC | UP | 0.64 | open |  |
| 11-22 12:33 | +10 stop | NEAR | UP | 0.67 | 0.50 | -2.04 |
| 11-22 12:33 | +20 | NEAR | UP | 0.67 | open |  |
| 11-22 12:33 | +15 | NEAR | UP | 0.67 | open |  |
| 11-22 12:33 | +10 | NEAR | UP | 0.67 | open |  |
| 11-22 12:33 | +5 | NEAR | UP | 0.67 | open |  |
| 11-22 12:23 | +10 stop | BNB | DOWN | 0.60 | 0.81 | 1.82 |
| 11-22 12:23 | +20 | BNB | DOWN | 0.60 | 0.81 | 1.82 |
| 11-22 12:23 | +15 | BNB | DOWN | 0.60 | 0.81 | 1.82 |
| 11-22 12:23 | +10 | BNB | DOWN | 0.61 | 0.81 | 1.72 |
| 11-22 12:23 | +5 | BNB | DOWN | 0.60 | 0.68 | 0.47 |
| 11-22 12:23 | +10 stop | NEAR | UP | 0.52 | 0.62 | 0.70 |
| 11-22 12:23 | +20 | NEAR | UP | 0.52 | no | -5.33 |
| 11-22 12:23 | +15 | NEAR | UP | 0.53 | no | -5.48 |
| 11-22 12:23 | +10 | NEAR | UP | 0.53 | no | -5.47 |
| 11-22 12:23 | +5 | NEAR | UP | 0.52 | 0.62 | 0.64 |
| 11-22 12:21 | +10 stop | ZEC | DOWN | 0.67 | 0.89 | 1.98 |
| 11-22 12:19 | +10 stop | ZEC | UP | 0.60 | 0.42 | -2.15 |
| 11-22 12:19 | +20 | ZEC | UP | 0.62 | no | -6.37 |
| 11-22 12:19 | +15 | ZEC | UP | 0.62 | no | -6.37 |
| 11-22 12:19 | +10 | ZEC | UP | 0.62 | no | -6.37 |
| 11-22 12:19 | +5 | ZEC | UP | 0.65 | no | -6.66 |
| 11-22 12:15 | +10 stop | XRP | UP | 0.68 | 0.78 | 0.71 |
| 11-22 12:15 | +20 | XRP | UP | 0.68 | no | -6.96 |
| 11-22 12:15 | +15 | XRP | UP | 0.68 | 0.83 | 1.24 |
| 11-22 12:15 | +10 | XRP | UP | 0.68 | 0.78 | 0.71 |
| 11-22 12:15 | +5 | XRP | UP | 0.68 | 0.78 | 0.71 |
| 11-22 12:14 | +10 stop | SOL | DOWN | 0.13 | 0.66 | 5.07 |
| 11-22 12:13 | +10 stop | ZEC | DOWN | 0.58 | 0.25 | -3.61 |
| 11-22 12:13 | +10 stop | SOL | UP | 0.52 | 0.68 | 1.26 |
| 11-22 12:12 | +10 stop | ZEC | UP | 0.35 | 0.57 | 1.86 |
| 11-22 12:11 | +10 stop | SOL | DOWN | 0.50 | 0.28 | -2.53 |
| 11-22 12:10 | +10 stop | ZEC | UP | 0.59 | 0.43 | -1.95 |
| 11-22 12:10 | +5 | ZEC | UP | 0.62 | 0.68 | 0.29 |
| 11-22 12:09 | +5 | HYPE | UP | 0.66 | 0.71 | 0.19 |
| 11-22 12:09 | +10 stop | HYPE | UP | 0.59 | 0.71 | 0.88 |
