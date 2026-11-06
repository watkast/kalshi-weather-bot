# Range-Scalp Bot

*Updated Fri Nov 06 01:30 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 48983 | 42680 | 6303 (75) | 1 | $-13930.82 | -4.5% |
| **+10¢** | 36572 | 29242 | 7330 (101) | 1 | $-12810.61 | -5.6% |
| **+15¢** | 30637 | 22746 | 7891 (130) | 1 | $-11670.95 | -6.1% |
| **+20¢** | 27226 | 18957 | 8269 (170) | 1 | $-10318.36 | -6.0% |
| **+10¢ (15¢ stop)** | 59723 | 59628 | 95 (57) | 1 | $-22114.22 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-06 01:30 | +10 stop | BNB | DOWN | 0.51 | open |  |
| 11-06 01:30 | +20 | BNB | DOWN | 0.51 | open |  |
| 11-06 01:30 | +15 | BNB | DOWN | 0.51 | open |  |
| 11-06 01:30 | +10 | BNB | DOWN | 0.51 | open |  |
| 11-06 01:30 | +5 | BNB | DOWN | 0.51 | open |  |
| 11-06 01:20 | +10 stop | ZEC | DOWN | 0.70 | 0.82 | 0.94 |
| 11-06 01:20 | +20 | ZEC | DOWN | 0.70 | 0.92 | 2.03 |
| 11-06 01:20 | +15 | ZEC | DOWN | 0.70 | 0.85 | 1.26 |
| 11-06 01:20 | +10 | ZEC | DOWN | 0.70 | 0.82 | 0.94 |
| 11-06 01:20 | +5 | ZEC | DOWN | 0.70 | 0.77 | 0.42 |
| 11-06 01:20 | +10 stop | BNB | DOWN | 0.58 | 0.69 | 0.77 |
| 11-06 01:20 | +15 | BNB | DOWN | 0.58 | 0.77 | 1.59 |
| 11-06 01:20 | +10 | BNB | DOWN | 0.58 | 0.69 | 0.77 |
| 11-06 01:20 | +5 | BNB | DOWN | 0.58 | 0.69 | 0.77 |
| 11-06 01:16 | +10 stop | HYPE | DOWN | 0.67 | 0.77 | 0.71 |
| 11-06 01:16 | +20 | HYPE | DOWN | 0.67 | 0.89 | 1.97 |
| 11-06 01:16 | +15 | HYPE | DOWN | 0.68 | 0.84 | 1.34 |
| 11-06 01:16 | +10 | HYPE | DOWN | 0.68 | 0.78 | 0.71 |
| 11-06 01:16 | +5 | HYPE | DOWN | 0.68 | 0.76 | 0.51 |
| 11-06 01:16 | +10 stop | DOGE | DOWN | 0.65 | 0.78 | 1.01 |
| 11-06 01:16 | +20 | DOGE | DOWN | 0.65 | 0.86 | 1.85 |
| 11-06 01:16 | +15 | DOGE | DOWN | 0.65 | 0.80 | 1.22 |
| 11-06 01:16 | +10 | DOGE | DOWN | 0.65 | 0.78 | 1.01 |
| 11-06 01:16 | +5 | DOGE | DOWN | 0.65 | 0.71 | 0.29 |
| 11-06 01:16 | +10 stop | BNB | DOWN | 0.67 | 0.81 | 1.13 |
| 11-06 01:16 | +20 | BNB | DOWN | 0.67 | 0.88 | 1.86 |
| 11-06 01:16 | +15 | BNB | DOWN | 0.67 | 0.83 | 1.34 |
| 11-06 01:16 | +10 | BNB | DOWN | 0.67 | 0.81 | 1.13 |
| 11-06 01:16 | +5 | BNB | DOWN | 0.67 | 0.73 | 0.30 |
| 11-06 01:16 | +10 stop | ZEC | DOWN | 0.63 | 0.75 | 0.89 |
| 11-06 01:16 | +20 | ZEC | DOWN | 0.63 | 0.84 | 1.83 |
| 11-06 01:16 | +15 | ZEC | DOWN | 0.63 | 0.79 | 1.31 |
| 11-06 01:16 | +10 | ZEC | DOWN | 0.63 | 0.75 | 0.89 |
| 11-06 01:16 | +5 | ZEC | DOWN | 0.63 | 0.68 | 0.17 |
| 11-06 01:16 | +10 stop | SOL | DOWN | 0.70 | 0.80 | 0.73 |
| 11-06 01:16 | +20 | SOL | DOWN | 0.70 | 0.92 | 1.99 |
| 11-06 01:16 | +15 | SOL | DOWN | 0.70 | 0.85 | 1.26 |
| 11-06 01:16 | +10 | SOL | DOWN | 0.70 | 0.80 | 0.73 |
| 11-06 01:16 | +5 | SOL | DOWN | 0.70 | 0.76 | 0.32 |
| 11-06 01:16 | +10 stop | ETH | DOWN | 0.71 | 0.82 | 0.84 |
