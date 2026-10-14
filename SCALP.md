# Range-Scalp Bot

*Updated Wed Oct 14 12:34 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 15966 | 13831 | 2135 (27) | 0 | $-5040.43 | -5.0% |
| **+10¢** | 12078 | 9601 | 2477 (39) | 0 | $-4664.67 | -6.1% |
| **+15¢** | 10157 | 7498 | 2659 (58) | 0 | $-4172.00 | -6.5% |
| **+20¢** | 9035 | 6245 | 2790 (75) | 0 | $-3709.45 | -6.5% |
| **+10¢ (15¢ stop)** | 19636 | 19586 | 50 (29) | 0 | $-7543.19 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-14 12:28 | +10 stop | ETH | UP | 0.54 | 0.29 | -2.83 |
| 10-14 12:28 | +20 | ETH | UP | 0.55 | no | -5.68 |
| 10-14 12:28 | +15 | ETH | UP | 0.55 | no | -5.68 |
| 10-14 12:28 | +10 | ETH | UP | 0.54 | no | -5.58 |
| 10-14 12:28 | +5 | ETH | UP | 0.55 | 0.61 | 0.28 |
| 10-14 12:27 | +10 stop | NEAR | DOWN | 0.27 | 0.64 | 3.39 |
| 10-14 12:27 | +20 | NEAR | DOWN | 0.27 | 0.64 | 3.39 |
| 10-14 12:27 | +15 | NEAR | DOWN | 0.27 | 0.64 | 3.39 |
| 10-14 12:27 | +10 | NEAR | DOWN | 0.27 | 0.64 | 3.39 |
| 10-14 12:27 | +5 | NEAR | DOWN | 0.27 | 0.64 | 3.39 |
| 10-14 12:21 | +10 stop | NEAR | DOWN | 0.62 | 0.76 | 1.10 |
| 10-14 12:21 | +10 | NEAR | DOWN | 0.62 | 0.76 | 1.10 |
| 10-14 12:21 | +5 | NEAR | DOWN | 0.62 | 0.76 | 1.10 |
| 10-14 12:19 | +5 | ZEC | DOWN | 0.69 | 0.74 | 0.21 |
| 10-14 12:18 | +15 | BTC | DOWN | 0.63 | 0.84 | 1.83 |
| 10-14 12:17 | +10 stop | NEAR | DOWN | 0.58 | 0.70 | 0.87 |
| 10-14 12:17 | +20 | NEAR | DOWN | 0.58 | 0.82 | 2.11 |
| 10-14 12:17 | +15 | NEAR | DOWN | 0.58 | 0.76 | 1.49 |
| 10-14 12:17 | +10 | NEAR | DOWN | 0.58 | 0.70 | 0.87 |
| 10-14 12:17 | +5 | NEAR | DOWN | 0.58 | 0.70 | 0.87 |
| 10-14 12:17 | +10 stop | BTC | DOWN | 0.65 | 0.77 | 0.91 |
| 10-14 12:17 | +10 | BTC | DOWN | 0.65 | 0.77 | 0.91 |
| 10-14 12:17 | +5 | BTC | DOWN | 0.65 | 0.70 | 0.19 |
| 10-14 12:17 | +5 | ETH | DOWN | 0.67 | 0.78 | 0.81 |
| 10-14 12:17 | +5 | BNB | DOWN | 0.68 | 0.75 | 0.40 |
| 10-14 12:17 | +10 stop | DOGE | DOWN | 0.70 | 0.80 | 0.73 |
| 10-14 12:17 | +20 | DOGE | DOWN | 0.70 | 0.92 | 1.96 |
| 10-14 12:17 | +15 | DOGE | DOWN | 0.70 | 0.88 | 1.57 |
| 10-14 12:17 | +10 | DOGE | DOWN | 0.70 | 0.80 | 0.73 |
| 10-14 12:17 | +5 | DOGE | DOWN | 0.70 | 0.80 | 0.73 |
| 10-14 12:16 | +10 stop | BTC | DOWN | 0.54 | 0.64 | 0.65 |
| 10-14 12:16 | +20 | BTC | DOWN | 0.54 | 0.77 | 1.99 |
| 10-14 12:16 | +15 | BTC | DOWN | 0.54 | 0.69 | 1.17 |
| 10-14 12:16 | +10 | BTC | DOWN | 0.54 | 0.64 | 0.65 |
| 10-14 12:16 | +5 | BTC | DOWN | 0.54 | 0.64 | 0.65 |
| 10-14 12:15 | +10 stop | SOL | DOWN | 0.59 | 0.71 | 0.88 |
| 10-14 12:15 | +20 | SOL | DOWN | 0.59 | 0.79 | 1.71 |
| 10-14 12:15 | +15 | SOL | DOWN | 0.59 | 0.76 | 1.40 |
| 10-14 12:15 | +10 | SOL | DOWN | 0.59 | 0.71 | 0.88 |
| 10-14 12:15 | +5 | SOL | DOWN | 0.59 | 0.71 | 0.88 |
