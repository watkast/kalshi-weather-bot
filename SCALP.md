# Range-Scalp Bot

*Updated Fri Oct 23 18:10 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 30734 | 26778 | 3956 (39) | 0 | $-8924.09 | -4.6% |
| **+10¢** | 23004 | 18433 | 4571 (56) | 0 | $-7938.57 | -5.5% |
| **+15¢** | 19246 | 14325 | 4921 (79) | 0 | $-7181.65 | -5.9% |
| **+20¢** | 17046 | 11894 | 5152 (102) | 0 | $-6414.84 | -6.0% |
| **+10¢ (15¢ stop)** | 37709 | 37650 | 59 (32) | 0 | $-14364.28 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-23 18:06 | +15 | ZEC | DOWN | 0.71 | 0.90 | 1.68 |
| 10-23 18:06 | +10 | ZEC | DOWN | 0.71 | 0.83 | 0.95 |
| 10-23 18:06 | +5 | ZEC | DOWN | 0.71 | 0.77 | 0.32 |
| 10-23 18:02 | +10 stop | ZEC | DOWN | 0.57 | 0.73 | 1.28 |
| 10-23 18:02 | +10 stop | NEAR | DOWN | 0.62 | 0.73 | 0.79 |
| 10-23 18:02 | +20 | NEAR | DOWN | 0.62 | 0.84 | 1.93 |
| 10-23 18:02 | +15 | NEAR | DOWN | 0.62 | 0.79 | 1.41 |
| 10-23 18:02 | +10 | NEAR | DOWN | 0.62 | 0.73 | 0.79 |
| 10-23 18:02 | +5 | NEAR | DOWN | 0.62 | 0.73 | 0.79 |
| 10-23 18:02 | +10 stop | HYPE | DOWN | 0.66 | 0.77 | 0.81 |
| 10-23 18:02 | +20 | HYPE | DOWN | 0.66 | 0.86 | 1.75 |
| 10-23 18:02 | +15 | HYPE | DOWN | 0.66 | 0.83 | 1.44 |
| 10-23 18:02 | +10 | HYPE | DOWN | 0.66 | 0.77 | 0.81 |
| 10-23 18:02 | +5 | HYPE | DOWN | 0.66 | 0.73 | 0.40 |
| 10-23 18:02 | +10 stop | SOL | DOWN | 0.68 | 0.82 | 1.13 |
| 10-23 18:02 | +20 | SOL | DOWN | 0.68 | 0.88 | 1.76 |
| 10-23 18:02 | +15 | SOL | DOWN | 0.68 | 0.85 | 1.45 |
| 10-23 18:02 | +10 | SOL | DOWN | 0.68 | 0.82 | 1.13 |
| 10-23 18:02 | +5 | SOL | DOWN | 0.68 | 0.77 | 0.61 |
| 10-23 18:02 | +10 stop | ETH | DOWN | 0.65 | 0.76 | 0.81 |
| 10-23 18:02 | +20 | ETH | DOWN | 0.65 | 0.87 | 1.96 |
| 10-23 18:02 | +15 | ETH | DOWN | 0.65 | 0.84 | 1.64 |
| 10-23 18:02 | +10 | ETH | DOWN | 0.65 | 0.76 | 0.81 |
| 10-23 18:02 | +5 | ETH | DOWN | 0.65 | 0.72 | 0.39 |
| 10-23 18:01 | +10 stop | BNB | DOWN | 0.68 | 0.85 | 1.45 |
| 10-23 18:01 | +20 | BNB | DOWN | 0.68 | 0.89 | 1.87 |
| 10-23 18:01 | +15 | BNB | DOWN | 0.68 | 0.85 | 1.45 |
| 10-23 18:01 | +10 | BNB | DOWN | 0.68 | 0.85 | 1.45 |
| 10-23 18:01 | +5 | BNB | DOWN | 0.68 | 0.73 | 0.20 |
| 10-23 18:01 | +10 stop | ZEC | DOWN | 0.71 | 0.54 | -2.03 |
| 10-23 18:01 | +20 | ZEC | DOWN | 0.71 | 0.91 | 1.82 |
| 10-23 18:01 | +15 | ZEC | DOWN | 0.71 | 0.87 | 1.37 |
| 10-23 18:01 | +10 | ZEC | DOWN | 0.71 | 0.85 | 1.16 |
| 10-23 18:01 | +5 | ZEC | DOWN | 0.71 | 0.76 | 0.22 |
| 10-23 18:01 | +10 stop | XRP | DOWN | 0.69 | 0.80 | 0.83 |
| 10-23 18:01 | +20 | XRP | DOWN | 0.69 | 0.90 | 1.90 |
| 10-23 18:01 | +15 | XRP | DOWN | 0.69 | 0.84 | 1.25 |
| 10-23 18:01 | +10 | XRP | DOWN | 0.69 | 0.80 | 0.83 |
| 10-23 18:01 | +5 | XRP | DOWN | 0.69 | 0.75 | 0.31 |
| 10-23 17:57 | +5 | BTC | UP | 0.52 | 0.67 | 1.16 |
