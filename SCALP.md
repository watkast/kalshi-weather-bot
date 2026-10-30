# Range-Scalp Bot

*Updated Fri Oct 30 01:57 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 40034 | 34972 | 5062 (51) | 0 | $-10955.44 | -4.3% |
| **+10¢** | 29838 | 23980 | 5858 (74) | 0 | $-9701.75 | -5.2% |
| **+15¢** | 24953 | 18650 | 6303 (101) | 1 | $-8685.68 | -5.5% |
| **+20¢** | 22141 | 15531 | 6610 (130) | 1 | $-7615.95 | -5.5% |
| **+10¢ (15¢ stop)** | 48851 | 48781 | 70 (37) | 0 | $-18468.17 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-30 01:55 | +10 stop | SOL | DOWN | 0.56 | 0.80 | 2.10 |
| 10-30 01:55 | +15 | SOL | DOWN | 0.55 | 0.80 | 2.21 |
| 10-30 01:55 | +10 | SOL | DOWN | 0.55 | 0.80 | 2.20 |
| 10-30 01:55 | +5 | SOL | DOWN | 0.55 | 0.63 | 0.45 |
| 10-30 01:53 | +10 stop | HYPE | UP | 0.68 | 0.50 | -2.14 |
| 10-30 01:52 | +10 | BNB | DOWN | 0.66 | 0.76 | 0.71 |
| 10-30 01:51 | +5 | BNB | DOWN | 0.71 | 0.76 | 0.22 |
| 10-30 01:51 | +10 stop | HYPE | UP | 0.70 | 0.50 | -2.33 |
| 10-30 01:50 | +10 stop | BNB | DOWN | 0.67 | 0.49 | -2.18 |
| 10-30 01:50 | +10 stop | SOL | DOWN | 0.66 | 0.82 | 1.33 |
| 10-30 01:50 | +5 | SOL | DOWN | 0.67 | 0.74 | 0.40 |
| 10-30 01:50 | +10 stop | ETH | DOWN | 0.70 | 0.83 | 1.05 |
| 10-30 01:50 | +15 | ETH | DOWN | 0.70 | 0.87 | 1.47 |
| 10-30 01:50 | +10 | ETH | DOWN | 0.70 | 0.83 | 1.05 |
| 10-30 01:50 | +5 | ETH | DOWN | 0.70 | 0.78 | 0.52 |
| 10-30 01:50 | +10 stop | DOGE | DOWN | 0.70 | 0.81 | 0.84 |
| 10-30 01:50 | +15 | DOGE | DOWN | 0.70 | 0.88 | 1.57 |
| 10-30 01:50 | +10 | DOGE | DOWN | 0.70 | 0.81 | 0.84 |
| 10-30 01:50 | +5 | DOGE | DOWN | 0.70 | 0.81 | 0.84 |
| 10-30 01:50 | +10 stop | ZEC | DOWN | 0.59 | 0.69 | 0.68 |
| 10-30 01:50 | +15 | ZEC | DOWN | 0.59 | 0.77 | 1.50 |
| 10-30 01:50 | +10 | ZEC | DOWN | 0.59 | 0.69 | 0.68 |
| 10-30 01:50 | +5 | ZEC | DOWN | 0.59 | 0.69 | 0.68 |
| 10-30 01:49 | +5 | SOL | DOWN | 0.48 | 0.56 | 0.44 |
| 10-30 01:49 | +10 stop | BNB | DOWN | 0.59 | 0.41 | -2.14 |
| 10-30 01:49 | +10 | BNB | DOWN | 0.59 | 0.69 | 0.68 |
| 10-30 01:49 | +5 | BNB | DOWN | 0.60 | 0.65 | 0.17 |
| 10-30 01:49 | +10 stop | HYPE | DOWN | 0.55 | 0.33 | -2.54 |
| 10-30 01:49 | +20 | HYPE | DOWN | 0.55 | 0.81 | 2.31 |
| 10-30 01:49 | +15 | HYPE | DOWN | 0.55 | 0.72 | 1.37 |
| 10-30 01:49 | +10 | HYPE | DOWN | 0.55 | 0.72 | 1.37 |
| 10-30 01:49 | +5 | HYPE | DOWN | 0.55 | 0.60 | 0.15 |
| 10-30 01:47 | +5 | ZEC | DOWN | 0.69 | 0.75 | 0.31 |
| 10-30 01:46 | +10 stop | NEAR | DOWN | 0.67 | 0.79 | 0.92 |
| 10-30 01:46 | +20 | NEAR | DOWN | 0.67 | 0.87 | 1.76 |
| 10-30 01:46 | +15 | NEAR | DOWN | 0.67 | 0.84 | 1.44 |
| 10-30 01:46 | +10 | NEAR | DOWN | 0.67 | 0.79 | 0.92 |
| 10-30 01:46 | +5 | NEAR | DOWN | 0.67 | 0.74 | 0.40 |
| 10-30 01:46 | +10 stop | DOGE | DOWN | 0.68 | 0.80 | 0.92 |
| 10-30 01:46 | +20 | DOGE | DOWN | 0.68 | 0.88 | 1.76 |
