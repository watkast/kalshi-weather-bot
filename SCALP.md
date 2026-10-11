# Range-Scalp Bot

*Updated Sun Oct 11 03:11 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 11300 | 9748 | 1552 (23) | 0 | $-3801.15 | -5.3% |
| **+10¢** | 8563 | 6758 | 1805 (36) | 0 | $-3608.35 | -6.7% |
| **+15¢** | 7215 | 5305 | 1910 (52) | 0 | $-3047.08 | -6.7% |
| **+20¢** | 6425 | 4437 | 1988 (66) | 0 | $-2551.57 | -6.3% |
| **+10¢ (15¢ stop)** | 13916 | 13875 | 41 (25) | 0 | $-5576.26 | -6.4% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-11 03:03 | +10 stop | DOGE | DOWN | 0.66 | 0.84 | 1.52 |
| 10-11 03:03 | +20 | DOGE | DOWN | 0.66 | 0.87 | 1.84 |
| 10-11 03:03 | +15 | DOGE | DOWN | 0.66 | 0.84 | 1.52 |
| 10-11 03:03 | +10 | DOGE | DOWN | 0.66 | 0.84 | 1.54 |
| 10-11 03:03 | +5 | DOGE | DOWN | 0.66 | 0.73 | 0.40 |
| 10-11 03:03 | +10 stop | HYPE | DOWN | 0.55 | 0.70 | 1.17 |
| 10-11 03:03 | +20 | HYPE | DOWN | 0.55 | 0.79 | 2.10 |
| 10-11 03:03 | +15 | HYPE | DOWN | 0.57 | 0.74 | 1.38 |
| 10-11 03:03 | +10 | HYPE | DOWN | 0.57 | 0.70 | 0.97 |
| 10-11 03:03 | +5 | HYPE | DOWN | 0.57 | 0.70 | 0.97 |
| 10-11 03:03 | +10 stop | BNB | DOWN | 0.67 | 0.82 | 1.23 |
| 10-11 03:03 | +20 | BNB | DOWN | 0.67 | 0.88 | 1.86 |
| 10-11 03:03 | +15 | BNB | DOWN | 0.67 | 0.82 | 1.23 |
| 10-11 03:03 | +10 | BNB | DOWN | 0.67 | 0.82 | 1.23 |
| 10-11 03:03 | +5 | BNB | DOWN | 0.67 | 0.82 | 1.23 |
| 10-11 03:02 | +5 | SOL | DOWN | 0.68 | 0.76 | 0.51 |
| 10-11 03:01 | +10 stop | NEAR | DOWN | 0.67 | 0.84 | 1.47 |
| 10-11 03:01 | +20 | NEAR | DOWN | 0.67 | 0.90 | 2.10 |
| 10-11 03:01 | +15 | NEAR | DOWN | 0.67 | 0.84 | 1.47 |
| 10-11 03:01 | +10 | NEAR | DOWN | 0.67 | 0.84 | 1.47 |
| 10-11 03:01 | +5 | NEAR | DOWN | 0.67 | 0.84 | 1.47 |
| 10-11 03:01 | +10 stop | SOL | DOWN | 0.56 | 0.69 | 0.97 |
| 10-11 03:01 | +20 | SOL | DOWN | 0.56 | 0.76 | 1.69 |
| 10-11 03:01 | +15 | SOL | DOWN | 0.56 | 0.72 | 1.27 |
| 10-11 03:01 | +10 | SOL | DOWN | 0.56 | 0.69 | 0.97 |
| 10-11 03:01 | +5 | SOL | DOWN | 0.56 | 0.62 | 0.25 |
| 10-11 03:01 | +10 stop | BTC | DOWN | 0.59 | 0.69 | 0.68 |
| 10-11 03:01 | +20 | BTC | DOWN | 0.59 | 0.79 | 1.71 |
| 10-11 03:01 | +15 | BTC | DOWN | 0.59 | 0.74 | 1.19 |
| 10-11 03:01 | +10 | BTC | DOWN | 0.59 | 0.69 | 0.68 |
| 10-11 03:01 | +5 | BTC | DOWN | 0.59 | 0.69 | 0.68 |
| 10-11 03:01 | +10 stop | ETH | DOWN | 0.68 | 0.83 | 1.24 |
| 10-11 03:01 | +20 | ETH | DOWN | 0.68 | 0.89 | 1.87 |
| 10-11 03:01 | +15 | ETH | DOWN | 0.68 | 0.83 | 1.24 |
| 10-11 03:01 | +10 | ETH | DOWN | 0.68 | 0.83 | 1.24 |
| 10-11 03:01 | +5 | ETH | DOWN | 0.68 | 0.75 | 0.40 |
| 10-11 02:55 | +5 | ZEC | DOWN | 0.54 | yes | -5.58 |
| 10-11 02:54 | +10 stop | ZEC | DOWN | 0.58 | 0.39 | -2.25 |
| 10-11 02:54 | +10 | ZEC | DOWN | 0.58 | yes | -5.98 |
| 10-11 02:54 | +5 | ZEC | DOWN | 0.58 | 0.66 | 0.46 |
