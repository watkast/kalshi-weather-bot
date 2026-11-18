# Range-Scalp Bot

*Updated Wed Nov 18 05:17 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 63644 | 55502 | 8142 (118) | 1 | $-17438.39 | -4.4% |
| **+10¢** | 47549 | 38020 | 9529 (159) | 1 | $-16362.20 | -5.5% |
| **+15¢** | 39869 | 29594 | 10275 (204) | 2 | $-14842.98 | -5.9% |
| **+20¢** | 35511 | 24728 | 10783 (259) | 2 | $-13113.96 | -5.9% |
| **+10¢ (15¢ stop)** | 77446 | 77288 | 158 (93) | 1 | $-28462.28 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-18 05:16 | +10 stop | BNB | UP | 0.68 | open |  |
| 11-18 05:16 | +20 | BNB | UP | 0.69 | open |  |
| 11-18 05:16 | +15 | BNB | UP | 0.69 | open |  |
| 11-18 05:16 | +10 | BNB | UP | 0.68 | open |  |
| 11-18 05:16 | +5 | BNB | UP | 0.68 | open |  |
| 11-18 05:15 | +10 stop | XRP | UP | 0.60 | 0.71 | 0.78 |
| 11-18 05:15 | +20 | XRP | UP | 0.60 | open |  |
| 11-18 05:15 | +15 | XRP | UP | 0.60 | open |  |
| 11-18 05:15 | +10 | XRP | UP | 0.60 | 0.71 | 0.78 |
| 11-18 05:15 | +5 | XRP | UP | 0.60 | 0.71 | 0.78 |
| 11-18 05:13 | +10 stop | NEAR | DOWN | 0.30 | 0.66 | 3.29 |
| 11-18 05:12 | +10 stop | NEAR | DOWN | 0.65 | 0.47 | -2.14 |
| 11-18 05:12 | +20 | NEAR | DOWN | 0.65 | yes | -6.66 |
| 11-18 05:12 | +15 | NEAR | DOWN | 0.65 | yes | -6.66 |
| 11-18 05:12 | +10 | NEAR | DOWN | 0.65 | yes | -6.66 |
| 11-18 05:12 | +5 | NEAR | DOWN | 0.65 | yes | -6.66 |
| 11-18 05:12 | +10 stop | DOGE | DOWN | 0.69 | 0.54 | -1.83 |
| 11-18 05:12 | +5 | DOGE | DOWN | 0.68 | 0.73 | 0.20 |
| 11-18 05:11 | +10 stop | XRP | DOWN | 0.68 | 0.48 | -2.34 |
| 11-18 05:11 | +20 | XRP | DOWN | 0.68 | yes | -6.96 |
| 11-18 05:11 | +15 | XRP | DOWN | 0.68 | yes | -6.96 |
| 11-18 05:11 | +10 | XRP | DOWN | 0.68 | yes | -6.96 |
| 11-18 05:11 | +5 | XRP | DOWN | 0.67 | yes | -6.90 |
| 11-18 05:10 | +10 | BNB | UP | 0.62 | 0.74 | 0.89 |
| 11-18 05:10 | +5 | BNB | UP | 0.62 | 0.69 | 0.38 |
| 11-18 05:10 | +10 stop | ETH | UP | 0.51 | 0.63 | 0.85 |
| 11-18 05:10 | +10 stop | DOGE | DOWN | 0.71 | 0.43 | -3.13 |
| 11-18 05:10 | +20 | DOGE | DOWN | 0.71 | yes | -7.25 |
| 11-18 05:10 | +15 | DOGE | DOWN | 0.71 | yes | -7.25 |
| 11-18 05:10 | +10 | DOGE | DOWN | 0.71 | yes | -7.25 |
| 11-18 05:10 | +5 | DOGE | DOWN | 0.71 | 0.77 | 0.32 |
| 11-18 05:10 | +10 stop | BNB | UP | 0.60 | 0.70 | 0.68 |
| 11-18 05:09 | +10 stop | BNB | UP | 0.48 | 0.32 | -1.94 |
| 11-18 05:08 | +10 stop | ETH | DOWN | 0.69 | 0.42 | -3.03 |
| 11-18 05:08 | +20 | ETH | DOWN | 0.70 | yes | -7.15 |
| 11-18 05:08 | +15 | ETH | DOWN | 0.69 | yes | -7.05 |
| 11-18 05:08 | +10 | ETH | DOWN | 0.69 | yes | -7.05 |
| 11-18 05:08 | +5 | ETH | DOWN | 0.68 | yes | -6.96 |
| 11-18 05:08 | +10 stop | BTC | DOWN | 0.55 | 0.27 | -3.12 |
| 11-18 05:08 | +15 | BTC | DOWN | 0.55 | yes | -5.68 |
