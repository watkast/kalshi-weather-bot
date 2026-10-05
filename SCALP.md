# Range-Scalp Bot

*Updated Mon Oct 05 04:43 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 3297 | 2826 | 471 (3) | 1 | $-1219.33 | -5.9% |
| **+10¢** | 2555 | 2021 | 534 (4) | 1 | $-1068.41 | -6.6% |
| **+15¢** | 2154 | 1588 | 566 (5) | 1 | $-963.97 | -7.1% |
| **+20¢** | 1923 | 1332 | 591 (10) | 1 | $-835.84 | -6.9% |
| **+10¢ (15¢ stop)** | 4096 | 4095 | 1 (1) | 1 | $-1586.44 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-05 04:43 | +10 stop | BNB | UP | 0.59 | open |  |
| 10-05 04:42 | +10 stop | BNB | UP | 0.49 | 0.62 | 0.95 |
| 10-05 04:38 | +10 stop | BNB | DOWN | 0.71 | 0.56 | -1.83 |
| 10-05 04:34 | +20 | NEAR | DOWN | 0.70 | 0.90 | 1.79 |
| 10-05 04:34 | +15 | NEAR | DOWN | 0.70 | 0.88 | 1.57 |
| 10-05 04:34 | +5 | NEAR | DOWN | 0.70 | 0.75 | 0.21 |
| 10-05 04:33 | +10 stop | BNB | DOWN | 0.68 | 0.47 | -2.39 |
| 10-05 04:32 | +10 stop | HYPE | DOWN | 0.69 | 0.43 | -2.93 |
| 10-05 04:32 | +10 stop | NEAR | DOWN | 0.71 | 0.82 | 0.85 |
| 10-05 04:32 | +10 | NEAR | DOWN | 0.69 | 0.79 | 0.74 |
| 10-05 04:32 | +5 | NEAR | DOWN | 0.69 | 0.76 | 0.43 |
| 10-05 04:32 | +10 stop | SOL | DOWN | 0.70 | 0.87 | 1.45 |
| 10-05 04:32 | +20 | SOL | DOWN | 0.70 | 0.92 | 1.92 |
| 10-05 04:32 | +15 | SOL | DOWN | 0.69 | 0.87 | 1.57 |
| 10-05 04:32 | +10 | SOL | DOWN | 0.69 | 0.80 | 0.83 |
| 10-05 04:32 | +5 | SOL | DOWN | 0.68 | 0.80 | 0.88 |
| 10-05 04:31 | +10 stop | BTC | DOWN | 0.60 | 0.75 | 1.19 |
| 10-05 04:31 | +20 | BTC | DOWN | 0.60 | 0.84 | 2.13 |
| 10-05 04:31 | +15 | BTC | DOWN | 0.60 | 0.75 | 1.19 |
| 10-05 04:31 | +10 | BTC | DOWN | 0.60 | 0.75 | 1.19 |
| 10-05 04:31 | +5 | BTC | DOWN | 0.60 | 0.68 | 0.47 |
| 10-05 04:31 | +10 stop | NEAR | DOWN | 0.50 | 0.62 | 0.85 |
| 10-05 04:31 | +20 | NEAR | DOWN | 0.50 | 0.76 | 2.29 |
| 10-05 04:31 | +15 | NEAR | DOWN | 0.50 | 0.76 | 2.29 |
| 10-05 04:31 | +10 | NEAR | DOWN | 0.50 | 0.62 | 0.85 |
| 10-05 04:31 | +5 | NEAR | DOWN | 0.50 | 0.62 | 0.85 |
| 10-05 04:31 | +10 stop | XRP | DOWN | 0.50 | 0.68 | 1.46 |
| 10-05 04:31 | +20 | XRP | DOWN | 0.50 | 0.77 | 2.39 |
| 10-05 04:31 | +15 | XRP | DOWN | 0.51 | 0.68 | 1.36 |
| 10-05 04:31 | +10 | XRP | DOWN | 0.51 | 0.68 | 1.36 |
| 10-05 04:31 | +5 | XRP | DOWN | 0.51 | 0.59 | 0.45 |
| 10-05 04:31 | +10 stop | ETH | DOWN | 0.58 | 0.84 | 2.32 |
| 10-05 04:31 | +20 | ETH | DOWN | 0.58 | 0.84 | 2.32 |
| 10-05 04:31 | +15 | ETH | DOWN | 0.58 | 0.84 | 2.32 |
| 10-05 04:31 | +10 | ETH | DOWN | 0.58 | 0.84 | 2.32 |
| 10-05 04:31 | +5 | ETH | DOWN | 0.58 | 0.64 | 0.25 |
| 10-05 04:31 | +10 stop | HYPE | UP | 0.68 | 0.41 | -3.03 |
| 10-05 04:31 | +20 | HYPE | UP | 0.67 | 0.87 | 1.77 |
| 10-05 04:31 | +15 | HYPE | UP | 0.67 | 0.82 | 1.24 |
| 10-05 04:31 | +10 | HYPE | UP | 0.67 | 0.77 | 0.72 |
