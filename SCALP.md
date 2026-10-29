# Range-Scalp Bot

*Updated Thu Oct 29 23:57 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 39908 | 34857 | 5051 (51) | 0 | $-10955.64 | -4.4% |
| **+10¢** | 29745 | 23903 | 5842 (74) | 0 | $-9689.35 | -5.2% |
| **+15¢** | 24872 | 18588 | 6284 (101) | 0 | $-8676.02 | -5.6% |
| **+20¢** | 22071 | 15481 | 6590 (130) | 0 | $-7599.08 | -5.5% |
| **+10¢ (15¢ stop)** | 48715 | 48645 | 70 (37) | 0 | $-18409.24 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-29 23:51 | +10 stop | ZEC | DOWN | 0.57 | 0.77 | 1.69 |
| 10-29 23:50 | +10 stop | ZEC | UP | 0.63 | 0.47 | -1.95 |
| 10-29 23:49 | +10 stop | ETH | DOWN | 0.65 | 0.82 | 1.43 |
| 10-29 23:49 | +20 | ETH | DOWN | 0.65 | 0.89 | 2.17 |
| 10-29 23:49 | +15 | ETH | DOWN | 0.65 | 0.82 | 1.43 |
| 10-29 23:49 | +10 | ETH | DOWN | 0.65 | 0.82 | 1.43 |
| 10-29 23:49 | +5 | ETH | DOWN | 0.65 | 0.73 | 0.50 |
| 10-29 23:49 | +10 stop | DOGE | DOWN | 0.71 | 0.82 | 0.84 |
| 10-29 23:49 | +20 | DOGE | DOWN | 0.71 | 0.92 | 1.90 |
| 10-29 23:49 | +15 | DOGE | DOWN | 0.71 | 0.89 | 1.58 |
| 10-29 23:49 | +10 | DOGE | DOWN | 0.71 | 0.82 | 0.84 |
| 10-29 23:49 | +5 | DOGE | DOWN | 0.71 | 0.82 | 0.84 |
| 10-29 23:49 | +10 stop | NEAR | DOWN | 0.51 | 0.61 | 0.65 |
| 10-29 23:49 | +10 | NEAR | DOWN | 0.51 | 0.61 | 0.65 |
| 10-29 23:49 | +5 | NEAR | DOWN | 0.52 | 0.60 | 0.45 |
| 10-29 23:48 | +10 stop | HYPE | DOWN | 0.60 | 0.71 | 0.78 |
| 10-29 23:48 | +20 | HYPE | DOWN | 0.60 | 0.83 | 2.03 |
| 10-29 23:48 | +15 | HYPE | DOWN | 0.59 | 0.76 | 1.40 |
| 10-29 23:48 | +10 | HYPE | DOWN | 0.59 | 0.69 | 0.68 |
| 10-29 23:48 | +5 | HYPE | DOWN | 0.59 | 0.64 | 0.16 |
| 10-29 23:47 | +5 | BNB | DOWN | 0.70 | 0.75 | 0.21 |
| 10-29 23:47 | +5 | BNB | DOWN | 0.60 | 0.66 | 0.28 |
| 10-29 23:46 | +10 stop | ZEC | DOWN | 0.68 | 0.47 | -2.44 |
| 10-29 23:46 | +20 | ZEC | DOWN | 0.69 | 0.89 | 1.81 |
| 10-29 23:46 | +15 | ZEC | DOWN | 0.70 | 0.87 | 1.50 |
| 10-29 23:46 | +10 | ZEC | DOWN | 0.70 | 0.87 | 1.50 |
| 10-29 23:46 | +5 | ZEC | DOWN | 0.70 | 0.77 | 0.45 |
| 10-29 23:46 | +10 stop | NEAR | DOWN | 0.67 | 0.77 | 0.71 |
| 10-29 23:46 | +20 | NEAR | DOWN | 0.67 | 0.87 | 1.76 |
| 10-29 23:46 | +15 | NEAR | DOWN | 0.67 | 0.85 | 1.55 |
| 10-29 23:46 | +10 | NEAR | DOWN | 0.67 | 0.77 | 0.71 |
| 10-29 23:46 | +5 | NEAR | DOWN | 0.67 | 0.72 | 0.19 |
| 10-29 23:46 | +10 stop | BNB | DOWN | 0.62 | 0.47 | -1.85 |
| 10-29 23:46 | +20 | BNB | DOWN | 0.62 | 0.86 | 2.14 |
| 10-29 23:46 | +15 | BNB | DOWN | 0.62 | 0.86 | 2.14 |
| 10-29 23:46 | +10 | BNB | DOWN | 0.62 | 0.75 | 0.99 |
| 10-29 23:46 | +5 | BNB | DOWN | 0.62 | 0.67 | 0.17 |
| 10-29 23:36 | +10 stop | XRP | DOWN | 0.64 | 0.78 | 1.15 |
| 10-29 23:36 | +10 stop | SOL | DOWN | 0.64 | 0.77 | 1.00 |
| 10-29 23:36 | +10 stop | BNB | DOWN | 0.64 | 0.74 | 0.69 |
