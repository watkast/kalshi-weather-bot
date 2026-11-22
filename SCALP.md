# Range-Scalp Bot

*Updated Sun Nov 22 11:53 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 68596 | 59853 | 8743 (142) | 5 | $-18473.61 | -4.3% |
| **+10¢** | 51219 | 41008 | 10211 (186) | 6 | $-17123.55 | -5.3% |
| **+15¢** | 42925 | 31920 | 11005 (237) | 6 | $-15358.12 | -5.7% |
| **+20¢** | 38213 | 26649 | 11564 (295) | 5 | $-13678.53 | -5.7% |
| **+10¢ (15¢ stop)** | 83555 | 83370 | 185 (116) | 1 | $-30781.38 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-22 11:52 | +10 stop | NEAR | DOWN | 0.65 | 0.49 | -1.95 |
| 11-22 11:52 | +5 | DOGE | UP | 0.68 | 0.79 | 0.82 |
| 11-22 11:52 | +10 stop | BTC | UP | 0.67 | 0.78 | 0.81 |
| 11-22 11:51 | +10 stop | DOGE | UP | 0.69 | 0.79 | 0.73 |
| 11-22 11:51 | +10 | DOGE | UP | 0.69 | 0.79 | 0.73 |
| 11-22 11:51 | +5 | DOGE | UP | 0.68 | 0.76 | 0.51 |
| 11-22 11:51 | +10 stop | NEAR | UP | 0.60 | 0.40 | -2.34 |
| 11-22 11:51 | +20 | NEAR | UP | 0.60 | open |  |
| 11-22 11:51 | +15 | NEAR | UP | 0.58 | open |  |
| 11-22 11:51 | +10 | NEAR | UP | 0.59 | open |  |
| 11-22 11:51 | +5 | NEAR | UP | 0.59 | open |  |
| 11-22 11:50 | +10 stop | XRP | UP | 0.66 | open |  |
| 11-22 11:50 | +20 | XRP | UP | 0.65 | open |  |
| 11-22 11:50 | +15 | XRP | UP | 0.65 | open |  |
| 11-22 11:50 | +10 | XRP | UP | 0.65 | open |  |
| 11-22 11:50 | +5 | XRP | UP | 0.65 | open |  |
| 11-22 11:50 | +10 stop | BTC | DOWN | 0.64 | 0.28 | -3.92 |
| 11-22 11:50 | +10 | BTC | DOWN | 0.64 | open |  |
| 11-22 11:50 | +5 | BTC | DOWN | 0.64 | open |  |
| 11-22 11:50 | +10 stop | ZEC | DOWN | 0.62 | 0.47 | -1.85 |
| 11-22 11:50 | +10 stop | SOL | DOWN | 0.62 | 0.45 | -2.05 |
| 11-22 11:50 | +10 | SOL | DOWN | 0.62 | open |  |
| 11-22 11:49 | +10 stop | ZEC | UP | 0.45 | 0.57 | 0.84 |
| 11-22 11:49 | +10 stop | SOL | UP | 0.46 | 0.61 | 1.15 |
| 11-22 11:49 | +10 | SOL | UP | 0.46 | 0.61 | 1.15 |
| 11-22 11:48 | +5 | BNB | UP | 0.59 | 0.84 | 2.21 |
| 11-22 11:48 | +10 stop | SOL | UP | 0.54 | 0.65 | 0.76 |
| 11-22 11:48 | +15 | SOL | UP | 0.54 | open |  |
| 11-22 11:48 | +10 | SOL | UP | 0.54 | 0.65 | 0.76 |
| 11-22 11:48 | +5 | ETH | UP | 0.61 | 0.80 | 1.61 |
| 11-22 11:48 | +5 | SOL | UP | 0.65 | open |  |
| 11-22 11:48 | +5 | BNB | UP | 0.54 | 0.59 | 0.15 |
| 11-22 11:47 | +10 stop | XRP | UP | 0.66 | 0.79 | 1.01 |
| 11-22 11:47 | +10 | XRP | UP | 0.66 | 0.79 | 1.01 |
| 11-22 11:47 | +5 | XRP | UP | 0.66 | 0.72 | 0.28 |
| 11-22 11:47 | +10 stop | DOGE | UP | 0.65 | 0.76 | 0.81 |
| 11-22 11:47 | +20 | DOGE | UP | 0.65 | 0.85 | 1.75 |
| 11-22 11:47 | +15 | DOGE | UP | 0.65 | 0.85 | 1.75 |
| 11-22 11:47 | +10 | DOGE | UP | 0.65 | 0.76 | 0.81 |
| 11-22 11:47 | +5 | DOGE | UP | 0.65 | 0.70 | 0.19 |
