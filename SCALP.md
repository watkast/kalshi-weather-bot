# Range-Scalp Bot

*Updated Mon Oct 19 07:29 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 23675 | 20586 | 3089 (30) | 3 | $-7068.96 | -4.7% |
| **+10¢** | 17802 | 14245 | 3557 (44) | 4 | $-6287.93 | -5.6% |
| **+15¢** | 14914 | 11083 | 3831 (66) | 4 | $-5696.48 | -6.1% |
| **+20¢** | 13202 | 9194 | 4008 (85) | 4 | $-5064.08 | -6.1% |
| **+10¢ (15¢ stop)** | 29144 | 29093 | 51 (30) | 0 | $-11032.70 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-19 07:29 | +10 stop | BNB | UP | 0.62 | 0.18 | -4.68 |
| 10-19 07:29 | +15 | BNB | UP | 0.62 | open |  |
| 10-19 07:29 | +10 | BNB | UP | 0.64 | open |  |
| 10-19 07:26 | +10 stop | BNB | UP | 0.58 | 0.69 | 0.77 |
| 10-19 07:26 | +10 | BNB | UP | 0.59 | 0.69 | 0.68 |
| 10-19 07:25 | +10 stop | DOGE | DOWN | 0.58 | 0.76 | 1.49 |
| 10-19 07:25 | +5 | HYPE | DOWN | 0.60 | 0.66 | 0.27 |
| 10-19 07:24 | +10 stop | ETH | DOWN | 0.59 | 0.83 | 2.13 |
| 10-19 07:24 | +10 stop | BTC | UP | 0.71 | 0.88 | 1.47 |
| 10-19 07:24 | +10 | BTC | UP | 0.71 | 0.88 | 1.47 |
| 10-19 07:24 | +5 | BTC | UP | 0.71 | 0.78 | 0.42 |
| 10-19 07:24 | +5 | BNB | UP | 0.69 | open |  |
| 10-19 07:23 | +10 stop | HYPE | DOWN | 0.68 | 0.80 | 0.88 |
| 10-19 07:23 | +5 | HYPE | DOWN | 0.59 | 0.70 | 0.74 |
| 10-19 07:23 | +10 stop | BTC | UP | 0.50 | 0.62 | 0.85 |
| 10-19 07:23 | +10 | BTC | UP | 0.50 | 0.62 | 0.85 |
| 10-19 07:23 | +5 | BTC | UP | 0.50 | 0.62 | 0.85 |
| 10-19 07:23 | +5 | BNB | UP | 0.45 | 0.58 | 0.94 |
| 10-19 07:22 | +10 stop | BNB | UP | 0.60 | 0.71 | 0.78 |
| 10-19 07:22 | +10 | BNB | UP | 0.59 | 0.71 | 0.83 |
| 10-19 07:22 | +5 | BNB | UP | 0.55 | 0.67 | 0.86 |
| 10-19 07:22 | +5 | HYPE | UP | 0.50 | 0.58 | 0.44 |
| 10-19 07:22 | +10 stop | HYPE | UP | 0.53 | 0.38 | -1.85 |
| 10-19 07:22 | +20 | HYPE | UP | 0.53 | open |  |
| 10-19 07:22 | +15 | HYPE | UP | 0.53 | open |  |
| 10-19 07:22 | +10 | HYPE | UP | 0.53 | open |  |
| 10-19 07:22 | +5 | HYPE | UP | 0.53 | 0.58 | 0.14 |
| 10-19 07:21 | +10 stop | BNB | UP | 0.48 | 0.67 | 1.56 |
| 10-19 07:21 | +10 | BNB | UP | 0.48 | 0.67 | 1.56 |
| 10-19 07:21 | +5 | BNB | UP | 0.48 | 0.54 | 0.24 |
| 10-19 07:21 | +10 stop | SOL | DOWN | 0.61 | 0.46 | -1.85 |
| 10-19 07:21 | +10 stop | BTC | UP | 0.63 | 0.75 | 0.89 |
| 10-19 07:21 | +15 | BTC | UP | 0.63 | 0.78 | 1.20 |
| 10-19 07:21 | +10 | BTC | UP | 0.63 | 0.75 | 0.89 |
| 10-19 07:21 | +5 | BTC | UP | 0.63 | 0.70 | 0.38 |
| 10-19 07:21 | +10 stop | BNB | DOWN | 0.44 | 0.58 | 1.04 |
| 10-19 07:21 | +15 | BNB | DOWN | 0.44 | 0.70 | 2.27 |
| 10-19 07:21 | +10 | BNB | DOWN | 0.44 | 0.58 | 1.04 |
| 10-19 07:21 | +5 | BNB | DOWN | 0.44 | 0.58 | 1.04 |
| 10-19 07:20 | +10 stop | XRP | UP | 0.70 | 0.82 | 0.94 |
