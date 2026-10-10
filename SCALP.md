# Range-Scalp Bot

*Updated Sat Oct 10 11:12 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 10334 | 8910 | 1424 (22) | 2 | $-3519.48 | -5.4% |
| **+10¢** | 7819 | 6160 | 1659 (35) | 1 | $-3367.66 | -6.8% |
| **+15¢** | 6596 | 4837 | 1759 (51) | 1 | $-2846.40 | -6.9% |
| **+20¢** | 5862 | 4031 | 1831 (65) | 2 | $-2416.49 | -6.6% |
| **+10¢ (15¢ stop)** | 12691 | 12653 | 38 (25) | 0 | $-4968.90 | -6.3% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-10 11:10 | +10 stop | ZEC | DOWN | 0.66 | 0.87 | 1.86 |
| 10-10 11:09 | +10 stop | NEAR | UP | 0.56 | 0.37 | -2.24 |
| 10-10 11:09 | +5 | HYPE | DOWN | 0.69 | 0.81 | 0.94 |
| 10-10 11:07 | +5 | ZEC | DOWN | 0.67 | 0.87 | 1.76 |
| 10-10 11:07 | +10 stop | NEAR | DOWN | 0.66 | 0.37 | -3.23 |
| 10-10 11:05 | +10 stop | HYPE | DOWN | 0.66 | 0.81 | 1.23 |
| 10-10 11:05 | +20 | HYPE | DOWN | 0.66 | 0.90 | 2.17 |
| 10-10 11:05 | +15 | HYPE | DOWN | 0.66 | 0.81 | 1.23 |
| 10-10 11:05 | +10 | HYPE | DOWN | 0.66 | 0.81 | 1.23 |
| 10-10 11:05 | +5 | HYPE | DOWN | 0.66 | 0.71 | 0.19 |
| 10-10 11:05 | +10 stop | NEAR | DOWN | 0.70 | 0.50 | -2.33 |
| 10-10 11:05 | +10 | NEAR | DOWN | 0.70 | 0.83 | 1.05 |
| 10-10 11:05 | +5 | NEAR | DOWN | 0.70 | 0.83 | 1.05 |
| 10-10 11:05 | +10 stop | DOGE | DOWN | 0.68 | 0.81 | 1.02 |
| 10-10 11:05 | +10 stop | ETH | DOWN | 0.70 | 0.80 | 0.73 |
| 10-10 11:05 | +15 | ETH | DOWN | 0.70 | 0.85 | 1.26 |
| 10-10 11:05 | +10 | ETH | DOWN | 0.70 | 0.80 | 0.73 |
| 10-10 11:05 | +5 | ETH | DOWN | 0.70 | 0.80 | 0.73 |
| 10-10 11:05 | +10 stop | BNB | DOWN | 0.61 | 0.72 | 0.78 |
| 10-10 11:05 | +10 stop | ZEC | DOWN | 0.67 | 0.47 | -2.38 |
| 10-10 11:05 | +15 | ZEC | DOWN | 0.67 | 0.87 | 1.78 |
| 10-10 11:05 | +10 | ZEC | DOWN | 0.67 | 0.87 | 1.78 |
| 10-10 11:05 | +5 | ZEC | DOWN | 0.67 | 0.72 | 0.21 |
| 10-10 11:04 | +10 stop | DOGE | DOWN | 0.69 | 0.49 | -2.33 |
| 10-10 11:04 | +10 | DOGE | DOWN | 0.69 | 0.81 | 0.94 |
| 10-10 11:03 | +10 stop | XRP | DOWN | 0.66 | 0.83 | 1.44 |
| 10-10 11:02 | +10 stop | ZEC | DOWN | 0.65 | 0.76 | 0.81 |
| 10-10 11:02 | +20 | ZEC | DOWN | 0.65 | 0.87 | 1.96 |
| 10-10 11:02 | +15 | ZEC | DOWN | 0.65 | 0.80 | 1.22 |
| 10-10 11:02 | +10 | ZEC | DOWN | 0.65 | 0.76 | 0.81 |
| 10-10 11:02 | +5 | ZEC | DOWN | 0.65 | 0.76 | 0.81 |
| 10-10 11:02 | +10 stop | SOL | DOWN | 0.64 | 0.77 | 1.00 |
| 10-10 11:02 | +20 | SOL | DOWN | 0.64 | 0.84 | 1.73 |
| 10-10 11:02 | +15 | SOL | DOWN | 0.64 | 0.79 | 1.21 |
| 10-10 11:02 | +10 | SOL | DOWN | 0.65 | 0.77 | 0.91 |
| 10-10 11:02 | +5 | SOL | DOWN | 0.65 | 0.77 | 0.91 |
| 10-10 11:02 | +10 stop | ETH | DOWN | 0.60 | 0.78 | 1.50 |
| 10-10 11:02 | +20 | ETH | DOWN | 0.60 | 0.80 | 1.71 |
| 10-10 11:02 | +15 | ETH | DOWN | 0.60 | 0.78 | 1.50 |
| 10-10 11:02 | +10 | ETH | DOWN | 0.60 | 0.78 | 1.50 |
