# Range-Scalp Bot

*Updated Fri Nov 06 06:15 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 49290 | 42948 | 6342 (75) | 0 | $-13986.80 | -4.5% |
| **+10¢** | 36804 | 29434 | 7370 (101) | 0 | $-12825.21 | -5.5% |
| **+15¢** | 30829 | 22893 | 7936 (130) | 0 | $-11704.15 | -6.0% |
| **+20¢** | 27406 | 19088 | 8318 (170) | 0 | $-10347.96 | -6.0% |
| **+10¢ (15¢ stop)** | 60099 | 60004 | 95 (57) | 0 | $-22255.91 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-06 06:05 | +10 stop | HYPE | DOWN | 0.59 | 0.71 | 0.88 |
| 11-06 06:05 | +10 stop | NEAR | DOWN | 0.70 | 0.83 | 1.05 |
| 11-06 06:05 | +20 | NEAR | DOWN | 0.70 | 0.90 | 1.78 |
| 11-06 06:05 | +15 | NEAR | DOWN | 0.70 | 0.86 | 1.36 |
| 11-06 06:05 | +10 | NEAR | DOWN | 0.70 | 0.83 | 1.05 |
| 11-06 06:05 | +5 | NEAR | DOWN | 0.70 | 0.75 | 0.21 |
| 11-06 06:05 | +10 stop | BNB | DOWN | 0.69 | 0.80 | 0.83 |
| 11-06 06:05 | +20 | BNB | DOWN | 0.69 | 0.92 | 2.06 |
| 11-06 06:05 | +15 | BNB | DOWN | 0.69 | 0.87 | 1.57 |
| 11-06 06:05 | +10 | BNB | DOWN | 0.69 | 0.80 | 0.83 |
| 11-06 06:05 | +5 | BNB | DOWN | 0.67 | 0.74 | 0.40 |
| 11-06 06:04 | +5 | ZEC | DOWN | 0.70 | 0.75 | 0.21 |
| 11-06 06:03 | +10 stop | ETH | DOWN | 0.68 | 0.78 | 0.71 |
| 11-06 06:03 | +20 | ETH | DOWN | 0.68 | 0.93 | 2.24 |
| 11-06 06:03 | +15 | ETH | DOWN | 0.68 | 0.84 | 1.34 |
| 11-06 06:03 | +10 | ETH | DOWN | 0.68 | 0.78 | 0.71 |
| 11-06 06:03 | +5 | ETH | DOWN | 0.68 | 0.76 | 0.51 |
| 11-06 06:03 | +10 stop | ZEC | DOWN | 0.57 | 0.72 | 1.17 |
| 11-06 06:03 | +20 | ZEC | DOWN | 0.57 | 0.79 | 1.90 |
| 11-06 06:03 | +15 | ZEC | DOWN | 0.57 | 0.72 | 1.17 |
| 11-06 06:03 | +10 | ZEC | DOWN | 0.57 | 0.72 | 1.17 |
| 11-06 06:03 | +5 | ZEC | DOWN | 0.57 | 0.62 | 0.15 |
| 11-06 06:03 | +10 stop | SOL | DOWN | 0.65 | 0.75 | 0.70 |
| 11-06 06:03 | +20 | SOL | DOWN | 0.63 | 0.85 | 1.94 |
| 11-06 06:03 | +15 | SOL | DOWN | 0.63 | 0.80 | 1.41 |
| 11-06 06:03 | +10 | SOL | DOWN | 0.63 | 0.75 | 0.89 |
| 11-06 06:03 | +5 | SOL | DOWN | 0.63 | 0.71 | 0.48 |
| 11-06 06:03 | +10 stop | BTC | DOWN | 0.68 | 0.84 | 1.34 |
| 11-06 06:03 | +10 | BTC | DOWN | 0.68 | 0.84 | 1.34 |
| 11-06 06:03 | +5 | BTC | DOWN | 0.68 | 0.73 | 0.20 |
| 11-06 06:01 | +10 stop | HYPE | DOWN | 0.70 | 0.52 | -2.13 |
| 11-06 06:01 | +20 | HYPE | DOWN | 0.70 | 0.92 | 1.98 |
| 11-06 06:01 | +15 | HYPE | DOWN | 0.70 | 0.87 | 1.47 |
| 11-06 06:01 | +10 | HYPE | DOWN | 0.70 | 0.81 | 0.84 |
| 11-06 06:01 | +5 | HYPE | DOWN | 0.70 | 0.81 | 0.84 |
| 11-06 06:01 | +10 stop | DOGE | DOWN | 0.68 | 0.78 | 0.71 |
| 11-06 06:01 | +20 | DOGE | DOWN | 0.68 | 0.88 | 1.76 |
| 11-06 06:01 | +15 | DOGE | DOWN | 0.68 | 0.85 | 1.45 |
| 11-06 06:01 | +10 | DOGE | DOWN | 0.68 | 0.78 | 0.71 |
| 11-06 06:01 | +5 | DOGE | DOWN | 0.68 | 0.78 | 0.71 |
