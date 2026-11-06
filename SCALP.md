# Range-Scalp Bot

*Updated Fri Nov 06 01:20 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 48981 | 42678 | 6303 (75) | 0 | $-13932.01 | -4.5% |
| **+10¢** | 36570 | 29240 | 7330 (101) | 0 | $-12812.32 | -5.6% |
| **+15¢** | 30635 | 22744 | 7891 (130) | 0 | $-11673.80 | -6.1% |
| **+20¢** | 27221 | 18952 | 8269 (170) | 4 | $-10328.10 | -6.0% |
| **+10¢ (15¢ stop)** | 59721 | 59626 | 95 (57) | 0 | $-22115.93 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-06 01:16 | +10 stop | HYPE | DOWN | 0.67 | 0.77 | 0.71 |
| 11-06 01:16 | +20 | HYPE | DOWN | 0.67 | open |  |
| 11-06 01:16 | +15 | HYPE | DOWN | 0.68 | 0.84 | 1.34 |
| 11-06 01:16 | +10 | HYPE | DOWN | 0.68 | 0.78 | 0.71 |
| 11-06 01:16 | +5 | HYPE | DOWN | 0.68 | 0.76 | 0.51 |
| 11-06 01:16 | +10 stop | DOGE | DOWN | 0.65 | 0.78 | 1.01 |
| 11-06 01:16 | +20 | DOGE | DOWN | 0.65 | 0.86 | 1.85 |
| 11-06 01:16 | +15 | DOGE | DOWN | 0.65 | 0.80 | 1.22 |
| 11-06 01:16 | +10 | DOGE | DOWN | 0.65 | 0.78 | 1.01 |
| 11-06 01:16 | +5 | DOGE | DOWN | 0.65 | 0.71 | 0.29 |
| 11-06 01:16 | +10 stop | BNB | DOWN | 0.67 | 0.81 | 1.13 |
| 11-06 01:16 | +20 | BNB | DOWN | 0.67 | open |  |
| 11-06 01:16 | +15 | BNB | DOWN | 0.67 | 0.83 | 1.34 |
| 11-06 01:16 | +10 | BNB | DOWN | 0.67 | 0.81 | 1.13 |
| 11-06 01:16 | +5 | BNB | DOWN | 0.67 | 0.73 | 0.30 |
| 11-06 01:16 | +10 stop | ZEC | DOWN | 0.63 | 0.75 | 0.89 |
| 11-06 01:16 | +20 | ZEC | DOWN | 0.63 | 0.84 | 1.83 |
| 11-06 01:16 | +15 | ZEC | DOWN | 0.63 | 0.79 | 1.31 |
| 11-06 01:16 | +10 | ZEC | DOWN | 0.63 | 0.75 | 0.89 |
| 11-06 01:16 | +5 | ZEC | DOWN | 0.63 | 0.68 | 0.17 |
| 11-06 01:16 | +10 stop | SOL | DOWN | 0.70 | 0.80 | 0.73 |
| 11-06 01:16 | +20 | SOL | DOWN | 0.70 | open |  |
| 11-06 01:16 | +15 | SOL | DOWN | 0.70 | 0.85 | 1.26 |
| 11-06 01:16 | +10 | SOL | DOWN | 0.70 | 0.80 | 0.73 |
| 11-06 01:16 | +5 | SOL | DOWN | 0.70 | 0.76 | 0.32 |
| 11-06 01:16 | +10 stop | ETH | DOWN | 0.71 | 0.82 | 0.84 |
| 11-06 01:16 | +20 | ETH | DOWN | 0.71 | open |  |
| 11-06 01:16 | +15 | ETH | DOWN | 0.71 | 0.86 | 1.26 |
| 11-06 01:16 | +10 | ETH | DOWN | 0.71 | 0.82 | 0.84 |
| 11-06 01:16 | +5 | ETH | DOWN | 0.71 | 0.77 | 0.32 |
| 11-06 01:16 | +10 stop | NEAR | DOWN | 0.65 | 0.78 | 1.01 |
| 11-06 01:16 | +20 | NEAR | DOWN | 0.65 | 0.85 | 1.75 |
| 11-06 01:16 | +15 | NEAR | DOWN | 0.65 | 0.81 | 1.33 |
| 11-06 01:16 | +10 | NEAR | DOWN | 0.65 | 0.78 | 1.01 |
| 11-06 01:16 | +5 | NEAR | DOWN | 0.65 | 0.71 | 0.29 |
| 11-06 01:16 | +10 stop | XRP | DOWN | 0.68 | 0.78 | 0.71 |
| 11-06 01:16 | +20 | XRP | DOWN | 0.68 | 0.89 | 1.87 |
| 11-06 01:16 | +15 | XRP | DOWN | 0.68 | 0.83 | 1.24 |
| 11-06 01:16 | +10 | XRP | DOWN | 0.68 | 0.78 | 0.71 |
| 11-06 01:16 | +5 | XRP | DOWN | 0.68 | 0.73 | 0.20 |
