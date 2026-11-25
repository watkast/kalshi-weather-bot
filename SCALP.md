# Range-Scalp Bot

*Updated Wed Nov 25 16:43 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 71772 | 62636 | 9136 (158) | 0 | $-19179.11 | -4.2% |
| **+10¢** | 53536 | 42871 | 10665 (203) | 0 | $-17762.53 | -5.3% |
| **+15¢** | 44841 | 33357 | 11484 (260) | 0 | $-15816.09 | -5.6% |
| **+20¢** | 39927 | 27834 | 12093 (326) | 0 | $-14191.16 | -5.7% |
| **+10¢ (15¢ stop)** | 87410 | 87201 | 209 (128) | 0 | $-32132.67 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-25 16:41 | +10 stop | ZEC | DOWN | 0.63 | 0.75 | 0.86 |
| 11-25 16:41 | +20 | ZEC | DOWN | 0.63 | 0.88 | 2.25 |
| 11-25 16:41 | +15 | ZEC | DOWN | 0.63 | 0.81 | 1.52 |
| 11-25 16:41 | +10 | ZEC | DOWN | 0.63 | 0.75 | 0.89 |
| 11-25 16:41 | +5 | ZEC | DOWN | 0.63 | 0.75 | 0.89 |
| 11-25 16:33 | +5 | HYPE | DOWN | 0.70 | 0.75 | 0.21 |
| 11-25 16:33 | +5 | NEAR | DOWN | 0.71 | 0.76 | 0.22 |
| 11-25 16:33 | +10 stop | ETH | DOWN | 0.63 | 0.75 | 0.89 |
| 11-25 16:32 | +5 | ETH | DOWN | 0.62 | 0.69 | 0.38 |
| 11-25 16:32 | +5 | ZEC | DOWN | 0.66 | 0.73 | 0.40 |
| 11-25 16:32 | +5 | BNB | DOWN | 0.70 | 0.75 | 0.24 |
| 11-25 16:32 | +5 | BTC | DOWN | 0.65 | 0.72 | 0.39 |
| 11-25 16:32 | +5 | DOGE | DOWN | 0.62 | 0.67 | 0.17 |
| 11-25 16:32 | +5 | XRP | DOWN | 0.67 | 0.73 | 0.30 |
| 11-25 16:32 | +5 | SOL | DOWN | 0.66 | 0.72 | 0.29 |
| 11-25 16:31 | +10 stop | ZEC | DOWN | 0.58 | 0.69 | 0.77 |
| 11-25 16:31 | +20 | ZEC | DOWN | 0.58 | 0.79 | 1.80 |
| 11-25 16:31 | +15 | ZEC | DOWN | 0.58 | 0.73 | 1.18 |
| 11-25 16:31 | +10 | ZEC | DOWN | 0.59 | 0.69 | 0.69 |
| 11-25 16:31 | +5 | ZEC | DOWN | 0.59 | 0.64 | 0.16 |
| 11-25 16:31 | +10 stop | BNB | DOWN | 0.65 | 0.82 | 1.38 |
| 11-25 16:31 | +20 | BNB | DOWN | 0.65 | 0.87 | 1.91 |
| 11-25 16:31 | +15 | BNB | DOWN | 0.65 | 0.82 | 1.38 |
| 11-25 16:31 | +10 | BNB | DOWN | 0.65 | 0.82 | 1.38 |
| 11-25 16:31 | +5 | BNB | DOWN | 0.65 | 0.70 | 0.20 |
| 11-25 16:31 | +10 stop | DOGE | DOWN | 0.63 | 0.75 | 0.89 |
| 11-25 16:31 | +20 | DOGE | DOWN | 0.62 | 0.82 | 1.72 |
| 11-25 16:31 | +15 | DOGE | DOWN | 0.62 | 0.77 | 1.20 |
| 11-25 16:31 | +10 | DOGE | DOWN | 0.62 | 0.72 | 0.68 |
| 11-25 16:31 | +5 | DOGE | DOWN | 0.62 | 0.68 | 0.27 |
| 11-25 16:31 | +10 stop | NEAR | DOWN | 0.61 | 0.73 | 0.89 |
| 11-25 16:31 | +20 | NEAR | DOWN | 0.61 | 0.82 | 1.82 |
| 11-25 16:31 | +15 | NEAR | DOWN | 0.61 | 0.76 | 1.20 |
| 11-25 16:31 | +10 | NEAR | DOWN | 0.61 | 0.73 | 0.89 |
| 11-25 16:31 | +5 | NEAR | DOWN | 0.61 | 0.69 | 0.48 |
| 11-25 16:31 | +10 stop | ETH | DOWN | 0.55 | 0.66 | 0.76 |
| 11-25 16:31 | +20 | ETH | DOWN | 0.56 | 0.78 | 1.89 |
| 11-25 16:31 | +15 | ETH | DOWN | 0.56 | 0.71 | 1.17 |
| 11-25 16:31 | +10 | ETH | DOWN | 0.57 | 0.69 | 0.87 |
| 11-25 16:31 | +5 | ETH | DOWN | 0.57 | 0.64 | 0.35 |
