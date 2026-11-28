# Range-Scalp Bot

*Updated Sat Nov 28 02:14 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 74223 | 64794 | 9429 (171) | 2 | $-19631.59 | -4.2% |
| **+10¢** | 55296 | 44279 | 11017 (217) | 3 | $-18253.76 | -5.3% |
| **+15¢** | 46304 | 34439 | 11865 (275) | 3 | $-16301.67 | -5.6% |
| **+20¢** | 41207 | 28710 | 12497 (342) | 3 | $-14708.70 | -5.7% |
| **+10¢ (15¢ stop)** | 90338 | 90119 | 219 (135) | 1 | $-33358.86 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-28 02:13 | +10 stop | BTC | UP | 0.64 | open |  |
| 11-28 02:13 | +10 | BTC | UP | 0.64 | open |  |
| 11-28 02:13 | +5 | BTC | UP | 0.64 | 0.69 | 0.18 |
| 11-28 02:12 | +10 stop | NEAR | DOWN | 0.50 | 0.28 | -2.53 |
| 11-28 02:11 | +10 | SOL | DOWN | 0.58 | open |  |
| 11-28 02:11 | +10 stop | SOL | DOWN | 0.57 | 0.32 | -2.84 |
| 11-28 02:11 | +10 stop | ETH | DOWN | 0.48 | 0.62 | 1.05 |
| 11-28 02:11 | +10 | SOL | DOWN | 0.55 | 0.66 | 0.76 |
| 11-28 02:10 | +10 stop | BTC | DOWN | 0.66 | 0.40 | -2.93 |
| 11-28 02:10 | +20 | SOL | UP | 0.46 | 0.67 | 1.76 |
| 11-28 02:10 | +15 | SOL | UP | 0.48 | 0.67 | 1.56 |
| 11-28 02:10 | +10 | SOL | UP | 0.48 | 0.58 | 0.64 |
| 11-28 02:09 | +5 | ETH | UP | 0.59 | 0.82 | 1.98 |
| 11-28 02:09 | +10 stop | ETH | UP | 0.59 | 0.42 | -2.05 |
| 11-28 02:09 | +10 stop | NEAR | DOWN | 0.66 | 0.82 | 1.33 |
| 11-28 02:09 | +10 stop | SOL | UP | 0.70 | 0.44 | -2.93 |
| 11-28 02:08 | +10 stop | BTC | DOWN | 0.68 | 0.50 | -2.14 |
| 11-28 02:08 | +10 stop | BNB | UP | 0.62 | 0.80 | 1.51 |
| 11-28 02:08 | +10 stop | XRP | UP | 0.63 | 0.81 | 1.52 |
| 11-28 02:08 | +10 stop | NEAR | DOWN | 0.66 | 0.51 | -1.87 |
| 11-28 02:07 | +10 stop | BTC | DOWN | 0.68 | 0.53 | -1.84 |
| 11-28 02:07 | +5 | ZEC | DOWN | 0.71 | 0.78 | 0.42 |
| 11-28 02:07 | +10 stop | XRP | UP | 0.57 | 0.68 | 0.76 |
| 11-28 02:06 | +10 stop | DOGE | UP | 0.63 | 0.73 | 0.69 |
| 11-28 02:06 | +10 stop | SOL | DOWN | 0.66 | 0.50 | -1.98 |
| 11-28 02:06 | +5 | SOL | DOWN | 0.66 | open |  |
| 11-28 02:06 | +5 | NEAR | UP | 0.59 | 0.71 | 0.83 |
| 11-28 02:06 | +10 stop | ZEC | DOWN | 0.64 | 0.78 | 1.10 |
| 11-28 02:06 | +10 | ZEC | DOWN | 0.64 | 0.78 | 1.10 |
| 11-28 02:06 | +5 | ZEC | DOWN | 0.64 | 0.69 | 0.18 |
| 11-28 02:06 | +10 stop | BNB | DOWN | 0.62 | 0.35 | -3.03 |
| 11-28 02:05 | +5 | NEAR | UP | 0.60 | 0.65 | 0.17 |
| 11-28 02:05 | +10 stop | NEAR | UP | 0.63 | 0.43 | -2.35 |
| 11-28 02:05 | +15 | NEAR | UP | 0.63 | 0.80 | 1.41 |
| 11-28 02:05 | +10 | NEAR | UP | 0.63 | 0.73 | 0.69 |
| 11-28 02:05 | +5 | NEAR | UP | 0.63 | 0.68 | 0.17 |
| 11-28 02:05 | +10 stop | SOL | DOWN | 0.65 | 0.76 | 0.81 |
| 11-28 02:05 | +10 stop | BNB | DOWN | 0.56 | 0.66 | 0.68 |
| 11-28 02:04 | +5 | SOL | DOWN | 0.67 | 0.76 | 0.59 |
| 11-28 02:03 | +10 stop | HYPE | DOWN | 0.62 | 0.74 | 0.89 |
