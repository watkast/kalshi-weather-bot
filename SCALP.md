# Range-Scalp Bot

*Updated Wed Nov 04 18:09 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 47354 | 41235 | 6119 (72) | 0 | $-13652.26 | -4.6% |
| **+10¢** | 35372 | 28272 | 7100 (97) | 0 | $-12491.54 | -5.6% |
| **+15¢** | 29622 | 21978 | 7644 (125) | 0 | $-11453.09 | -6.2% |
| **+20¢** | 26319 | 18314 | 8005 (165) | 0 | $-10100.59 | -6.1% |
| **+10¢ (15¢ stop)** | 57713 | 57620 | 93 (56) | 0 | $-21499.22 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-04 18:01 | +5 | HYPE | UP | 0.69 | 0.75 | 0.31 |
| 11-04 18:00 | +10 stop | NEAR | UP | 0.70 | 0.80 | 0.73 |
| 11-04 18:00 | +20 | NEAR | UP | 0.70 | 0.92 | 2.01 |
| 11-04 18:00 | +15 | NEAR | UP | 0.70 | 0.86 | 1.36 |
| 11-04 18:00 | +10 | NEAR | UP | 0.70 | 0.80 | 0.73 |
| 11-04 18:00 | +5 | NEAR | UP | 0.70 | 0.75 | 0.21 |
| 11-04 18:00 | +10 stop | HYPE | UP | 0.58 | 0.68 | 0.66 |
| 11-04 18:00 | +20 | HYPE | UP | 0.58 | 0.80 | 1.90 |
| 11-04 18:00 | +15 | HYPE | UP | 0.58 | 0.75 | 1.38 |
| 11-04 18:00 | +10 | HYPE | UP | 0.58 | 0.68 | 0.66 |
| 11-04 18:00 | +5 | HYPE | UP | 0.58 | 0.65 | 0.36 |
| 11-04 17:56 | +10 stop | DOGE | UP | 0.66 | 0.81 | 1.23 |
| 11-04 17:56 | +10 stop | NEAR | DOWN | 0.59 | 0.71 | 0.88 |
| 11-04 17:56 | +20 | NEAR | DOWN | 0.59 | 0.87 | 2.55 |
| 11-04 17:56 | +15 | NEAR | DOWN | 0.59 | 0.75 | 1.29 |
| 11-04 17:56 | +10 | NEAR | DOWN | 0.59 | 0.71 | 0.88 |
| 11-04 17:56 | +5 | NEAR | DOWN | 0.59 | 0.71 | 0.88 |
| 11-04 17:56 | +10 stop | ETH | DOWN | 0.60 | 0.70 | 0.68 |
| 11-04 17:55 | +10 stop | DOGE | DOWN | 0.64 | 0.42 | -2.55 |
| 11-04 17:55 | +10 stop | BNB | UP | 0.61 | 0.74 | 0.99 |
| 11-04 17:55 | +20 | BNB | UP | 0.61 | 0.82 | 1.82 |
| 11-04 17:55 | +15 | BNB | UP | 0.61 | 0.82 | 1.82 |
| 11-04 17:55 | +10 | BNB | UP | 0.61 | 0.74 | 0.99 |
| 11-04 17:55 | +5 | BNB | UP | 0.61 | 0.74 | 0.99 |
| 11-04 17:54 | +10 stop | SOL | UP | 0.51 | 0.35 | -1.94 |
| 11-04 17:54 | +5 | SOL | UP | 0.51 | 0.60 | 0.55 |
| 11-04 17:53 | +10 stop | HYPE | DOWN | 0.71 | 0.83 | 0.95 |
| 11-04 17:53 | +10 stop | BTC | UP | 0.67 | 0.80 | 1.02 |
| 11-04 17:53 | +10 stop | ZEC | UP | 0.60 | 0.35 | -2.83 |
| 11-04 17:53 | +10 stop | DOGE | UP | 0.63 | 0.40 | -2.64 |
| 11-04 17:53 | +10 stop | SOL | DOWN | 0.41 | 0.67 | 2.27 |
| 11-04 17:53 | +10 stop | ZEC | DOWN | 0.40 | 0.52 | 0.85 |
| 11-04 17:53 | +5 | SOL | DOWN | 0.49 | 0.67 | 1.46 |
| 11-04 17:53 | +10 stop | ETH | UP | 0.70 | 0.55 | -1.83 |
| 11-04 17:53 | +15 | ETH | UP | 0.70 | no | -7.15 |
| 11-04 17:53 | +10 | ETH | UP | 0.70 | no | -7.15 |
| 11-04 17:53 | +5 | ETH | UP | 0.70 | no | -7.15 |
| 11-04 17:52 | +10 | NEAR | DOWN | 0.61 | 0.71 | 0.68 |
| 11-04 17:52 | +10 stop | XRP | DOWN | 0.68 | 0.80 | 0.97 |
| 11-04 17:52 | +10 stop | BTC | UP | 0.58 | 0.69 | 0.77 |
