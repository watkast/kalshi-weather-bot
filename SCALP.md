# Range-Scalp Bot

*Updated Thu Nov 26 12:03 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 72635 | 63409 | 9226 (158) | 0 | $-19252.80 | -4.2% |
| **+10¢** | 54169 | 43395 | 10774 (203) | 0 | $-17832.90 | -5.2% |
| **+15¢** | 45357 | 33749 | 11608 (261) | 0 | $-15938.70 | -5.6% |
| **+20¢** | 40371 | 28148 | 12223 (327) | 0 | $-14322.09 | -5.7% |
| **+10¢ (15¢ stop)** | 88439 | 88230 | 209 (128) | 0 | $-32475.45 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-26 11:58 | +5 | NEAR | DOWN | 0.41 | 0.62 | 1.76 |
| 11-26 11:58 | +10 stop | BNB | DOWN | 0.54 | 0.84 | 2.72 |
| 11-26 11:58 | +15 | BNB | DOWN | 0.59 | 0.84 | 2.23 |
| 11-26 11:58 | +10 | BNB | DOWN | 0.59 | 0.84 | 2.23 |
| 11-26 11:58 | +5 | BNB | DOWN | 0.58 | 0.84 | 2.32 |
| 11-26 11:57 | +10 stop | DOGE | UP | 0.64 | 0.93 | 2.68 |
| 11-26 11:57 | +10 | DOGE | UP | 0.64 | 0.93 | 2.68 |
| 11-26 11:57 | +5 | DOGE | UP | 0.64 | 0.93 | 2.68 |
| 11-26 11:57 | +10 stop | NEAR | DOWN | 0.60 | 0.24 | -3.90 |
| 11-26 11:57 | +5 | NEAR | DOWN | 0.60 | 0.68 | 0.47 |
| 11-26 11:57 | +10 stop | ETH | DOWN | 0.63 | 0.79 | 1.31 |
| 11-26 11:57 | +20 | ETH | DOWN | 0.62 | 0.88 | 2.35 |
| 11-26 11:57 | +15 | ETH | DOWN | 0.62 | 0.79 | 1.41 |
| 11-26 11:57 | +10 | ETH | DOWN | 0.62 | 0.79 | 1.41 |
| 11-26 11:57 | +5 | ETH | DOWN | 0.61 | 0.79 | 1.51 |
| 11-26 11:56 | +10 stop | DOGE | DOWN | 0.48 | 0.62 | 1.05 |
| 11-26 11:56 | +10 | DOGE | DOWN | 0.47 | 0.62 | 1.15 |
| 11-26 11:56 | +5 | DOGE | DOWN | 0.48 | 0.62 | 1.05 |
| 11-26 11:55 | +10 stop | BNB | DOWN | 0.54 | 0.76 | 1.89 |
| 11-26 11:54 | +10 stop | SOL | UP | 0.64 | 0.74 | 0.71 |
| 11-26 11:54 | +10 stop | DOGE | UP | 0.54 | 0.30 | -2.73 |
| 11-26 11:54 | +5 | NEAR | DOWN | 0.62 | 0.67 | 0.17 |
| 11-26 11:54 | +10 stop | BTC | DOWN | 0.71 | 0.81 | 0.74 |
| 11-26 11:54 | +10 | BTC | DOWN | 0.71 | 0.81 | 0.74 |
| 11-26 11:54 | +5 | BTC | DOWN | 0.69 | 0.79 | 0.73 |
| 11-26 11:54 | +10 stop | ETH | DOWN | 0.68 | 0.84 | 1.31 |
| 11-26 11:54 | +15 | ETH | DOWN | 0.65 | 0.84 | 1.64 |
| 11-26 11:54 | +10 | ETH | DOWN | 0.65 | 0.76 | 0.81 |
| 11-26 11:54 | +5 | ETH | DOWN | 0.65 | 0.76 | 0.81 |
| 11-26 11:53 | +10 stop | BNB | UP | 0.61 | 0.36 | -2.84 |
| 11-26 11:53 | +10 | HYPE | DOWN | 0.57 | 0.70 | 0.97 |
| 11-26 11:53 | +10 stop | NEAR | DOWN | 0.58 | 0.80 | 1.90 |
| 11-26 11:53 | +5 | NEAR | DOWN | 0.58 | 0.66 | 0.46 |
| 11-26 11:53 | +10 stop | HYPE | DOWN | 0.60 | 0.70 | 0.68 |
| 11-26 11:52 | +10 | HYPE | DOWN | 0.50 | 0.67 | 1.36 |
| 11-26 11:52 | +10 stop | BTC | DOWN | 0.66 | 0.80 | 1.12 |
| 11-26 11:51 | +10 stop | BNB | UP | 0.70 | 0.55 | -1.83 |
| 11-26 11:51 | +10 stop | ETH | DOWN | 0.43 | 0.59 | 1.25 |
| 11-26 11:51 | +10 stop | HYPE | DOWN | 0.67 | 0.51 | -1.94 |
| 11-26 11:51 | +10 stop | BTC | DOWN | 0.69 | 0.51 | -2.13 |
