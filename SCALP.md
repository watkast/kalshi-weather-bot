# Range-Scalp Bot

*Updated Wed Nov 11 01:27 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 55188 | 48138 | 7050 (94) | 4 | $-15010.95 | -4.3% |
| **+10¢** | 41229 | 33004 | 8225 (124) | 6 | $-13941.09 | -5.4% |
| **+15¢** | 34566 | 25701 | 8865 (158) | 6 | $-12676.28 | -5.8% |
| **+20¢** | 30775 | 21474 | 9301 (207) | 6 | $-11083.62 | -5.7% |
| **+10¢ (15¢ stop)** | 67229 | 67111 | 118 (73) | 0 | $-24789.23 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-11 01:26 | +10 stop | DOGE | DOWN | 0.65 | 0.48 | -2.04 |
| 11-11 01:26 | +10 stop | XRP | UP | 0.55 | 0.66 | 0.76 |
| 11-11 01:24 | +10 stop | BNB | UP | 0.66 | 0.82 | 1.33 |
| 11-11 01:23 | +20 | XRP | UP | 0.62 | 0.82 | 1.72 |
| 11-11 01:23 | +15 | XRP | UP | 0.62 | 0.82 | 1.72 |
| 11-11 01:23 | +10 stop | DOGE | DOWN | 0.68 | 0.47 | -2.44 |
| 11-11 01:23 | +15 | DOGE | DOWN | 0.68 | open |  |
| 11-11 01:23 | +10 | DOGE | DOWN | 0.68 | open |  |
| 11-11 01:23 | +5 | DOGE | DOWN | 0.68 | open |  |
| 11-11 01:22 | +10 stop | SOL | UP | 0.63 | 0.79 | 1.31 |
| 11-11 01:21 | +10 stop | NEAR | DOWN | 0.70 | 0.47 | -2.63 |
| 11-11 01:21 | +5 | XRP | UP | 0.71 | 0.82 | 0.84 |
| 11-11 01:20 | +10 stop | ETH | UP | 0.69 | 0.81 | 0.94 |
| 11-11 01:20 | +10 stop | HYPE | DOWN | 0.51 | 0.32 | -2.24 |
| 11-11 01:20 | +10 stop | NEAR | DOWN | 0.60 | 0.43 | -2.05 |
| 11-11 01:20 | +10 stop | BNB | DOWN | 0.51 | 0.34 | -2.04 |
| 11-11 01:20 | +10 stop | XRP | UP | 0.66 | 0.49 | -2.04 |
| 11-11 01:20 | +10 | XRP | UP | 0.66 | 0.82 | 1.33 |
| 11-11 01:20 | +5 | XRP | UP | 0.56 | 0.65 | 0.56 |
| 11-11 01:20 | +10 stop | NEAR | UP | 0.35 | 0.60 | 2.17 |
| 11-11 01:20 | +5 | HYPE | UP | 0.68 | 0.81 | 1.03 |
| 11-11 01:20 | +10 stop | HYPE | UP | 0.70 | 0.40 | -3.32 |
| 11-11 01:19 | +10 stop | DOGE | DOWN | 0.66 | 0.82 | 1.33 |
| 11-11 01:19 | +10 | DOGE | DOWN | 0.66 | 0.82 | 1.33 |
| 11-11 01:19 | +5 | DOGE | DOWN | 0.66 | 0.82 | 1.33 |
| 11-11 01:19 | +5 | ETH | UP | 0.70 | 0.75 | 0.21 |
| 11-11 01:19 | +10 stop | XRP | UP | 0.55 | 0.65 | 0.66 |
| 11-11 01:19 | +20 | XRP | UP | 0.55 | 0.75 | 1.68 |
| 11-11 01:19 | +15 | XRP | UP | 0.55 | 0.70 | 1.17 |
| 11-11 01:19 | +10 | XRP | UP | 0.55 | 0.65 | 0.66 |
| 11-11 01:19 | +5 | XRP | UP | 0.55 | 0.62 | 0.35 |
| 11-11 01:18 | +5 | BTC | UP | 0.70 | 0.78 | 0.52 |
| 11-11 01:18 | +5 | SOL | DOWN | 0.59 | open |  |
| 11-11 01:18 | +10 stop | BNB | DOWN | 0.66 | 0.40 | -2.93 |
| 11-11 01:18 | +5 | BNB | DOWN | 0.66 | open |  |
| 11-11 01:17 | +10 stop | BTC | UP | 0.58 | 0.70 | 0.87 |
| 11-11 01:17 | +20 | BTC | UP | 0.58 | 0.78 | 1.69 |
| 11-11 01:17 | +15 | BTC | UP | 0.58 | 0.78 | 1.69 |
| 11-11 01:17 | +10 | BTC | UP | 0.58 | 0.70 | 0.87 |
| 11-11 01:17 | +5 | BTC | UP | 0.58 | 0.65 | 0.36 |
