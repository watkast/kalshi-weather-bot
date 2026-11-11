# Range-Scalp Bot

*Updated Wed Nov 11 18:57 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 56074 | 48900 | 7174 (94) | 1 | $-15331.25 | -4.3% |
| **+10¢** | 41898 | 33525 | 8373 (124) | 1 | $-14316.63 | -5.4% |
| **+15¢** | 35132 | 26106 | 9026 (158) | 1 | $-13028.47 | -5.9% |
| **+20¢** | 31293 | 21824 | 9469 (208) | 0 | $-11397.28 | -5.8% |
| **+10¢ (15¢ stop)** | 68317 | 68196 | 121 (73) | 0 | $-25153.51 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-11 18:54 | +10 stop | XRP | DOWN | 0.68 | 0.84 | 1.39 |
| 11-11 18:52 | +10 stop | XRP | UP | 0.62 | 0.46 | -1.94 |
| 11-11 18:52 | +15 | XRP | UP | 0.62 | open |  |
| 11-11 18:52 | +10 | XRP | UP | 0.62 | open |  |
| 11-11 18:52 | +5 | XRP | UP | 0.62 | open |  |
| 11-11 18:50 | +10 stop | ETH | DOWN | 0.63 | 0.82 | 1.62 |
| 11-11 18:50 | +10 stop | DOGE | DOWN | 0.62 | 0.76 | 1.10 |
| 11-11 18:49 | +10 stop | BNB | UP | 0.59 | 0.38 | -2.44 |
| 11-11 18:49 | +10 stop | BTC | DOWN | 0.61 | 0.76 | 1.20 |
| 11-11 18:49 | +5 | NEAR | DOWN | 0.68 | 0.79 | 0.82 |
| 11-11 18:49 | +5 | HYPE | DOWN | 0.71 | 0.78 | 0.42 |
| 11-11 18:49 | +10 stop | DOGE | UP | 0.56 | 0.41 | -1.85 |
| 11-11 18:48 | +5 | NEAR | DOWN | 0.60 | 0.69 | 0.58 |
| 11-11 18:48 | +5 | NEAR | DOWN | 0.59 | 0.69 | 0.68 |
| 11-11 18:47 | +5 | SOL | DOWN | 0.65 | 0.73 | 0.50 |
| 11-11 18:47 | +10 stop | SOL | DOWN | 0.63 | 0.73 | 0.69 |
| 11-11 18:47 | +20 | SOL | DOWN | 0.63 | 0.87 | 2.15 |
| 11-11 18:47 | +15 | SOL | DOWN | 0.63 | 0.87 | 2.15 |
| 11-11 18:47 | +10 | SOL | DOWN | 0.63 | 0.73 | 0.69 |
| 11-11 18:47 | +5 | SOL | DOWN | 0.63 | 0.69 | 0.28 |
| 11-11 18:45 | +10 stop | NEAR | DOWN | 0.66 | 0.79 | 1.02 |
| 11-11 18:45 | +20 | NEAR | DOWN | 0.66 | 0.87 | 1.86 |
| 11-11 18:45 | +15 | NEAR | DOWN | 0.66 | 0.81 | 1.23 |
| 11-11 18:45 | +10 | NEAR | DOWN | 0.66 | 0.79 | 1.02 |
| 11-11 18:45 | +5 | NEAR | DOWN | 0.66 | 0.71 | 0.19 |
| 11-11 18:45 | +10 stop | BNB | DOWN | 0.65 | 0.47 | -2.14 |
| 11-11 18:45 | +20 | BNB | DOWN | 0.65 | 0.90 | 2.28 |
| 11-11 18:45 | +15 | BNB | DOWN | 0.65 | 0.82 | 1.43 |
| 11-11 18:45 | +10 | BNB | DOWN | 0.65 | 0.82 | 1.43 |
| 11-11 18:45 | +5 | BNB | DOWN | 0.65 | 0.82 | 1.43 |
| 11-11 18:45 | +10 stop | BTC | DOWN | 0.66 | 0.48 | -2.14 |
| 11-11 18:45 | +20 | BTC | DOWN | 0.66 | 0.88 | 1.96 |
| 11-11 18:45 | +15 | BTC | DOWN | 0.66 | 0.83 | 1.44 |
| 11-11 18:45 | +10 | BTC | DOWN | 0.66 | 0.76 | 0.71 |
| 11-11 18:45 | +5 | BTC | DOWN | 0.66 | 0.76 | 0.71 |
| 11-11 18:45 | +10 stop | HYPE | DOWN | 0.68 | 0.78 | 0.72 |
| 11-11 18:45 | +20 | HYPE | DOWN | 0.68 | 0.88 | 1.76 |
| 11-11 18:45 | +15 | HYPE | DOWN | 0.68 | 0.85 | 1.45 |
| 11-11 18:45 | +10 | HYPE | DOWN | 0.68 | 0.78 | 0.71 |
| 11-11 18:45 | +5 | HYPE | DOWN | 0.68 | 0.73 | 0.20 |
