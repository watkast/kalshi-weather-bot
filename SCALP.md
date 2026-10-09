# Range-Scalp Bot

*Updated Fri Oct 09 10:22 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 8940 | 7732 | 1208 (13) | 0 | $-2943.87 | -5.2% |
| **+10¢** | 6765 | 5349 | 1416 (25) | 0 | $-2818.44 | -6.6% |
| **+15¢** | 5706 | 4214 | 1492 (37) | 0 | $-2291.55 | -6.4% |
| **+20¢** | 5077 | 3529 | 1548 (45) | 2 | $-1884.01 | -5.9% |
| **+10¢ (15¢ stop)** | 10893 | 10863 | 30 (19) | 0 | $-4082.91 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-09 10:19 | +5 | HYPE | DOWN | 0.63 | 0.69 | 0.28 |
| 10-09 10:18 | +5 | ZEC | DOWN | 0.64 | 0.70 | 0.28 |
| 10-09 10:17 | +5 | HYPE | DOWN | 0.54 | 0.60 | 0.25 |
| 10-09 10:17 | +10 stop | BNB | DOWN | 0.70 | 0.81 | 0.82 |
| 10-09 10:17 | +20 | BNB | DOWN | 0.70 | open |  |
| 10-09 10:17 | +15 | BNB | DOWN | 0.70 | 0.90 | 1.76 |
| 10-09 10:17 | +10 | BNB | DOWN | 0.70 | 0.81 | 0.81 |
| 10-09 10:17 | +5 | BNB | DOWN | 0.70 | 0.81 | 0.81 |
| 10-09 10:16 | +10 stop | ETH | DOWN | 0.63 | 0.75 | 0.91 |
| 10-09 10:16 | +20 | ETH | DOWN | 0.63 | 0.85 | 1.96 |
| 10-09 10:16 | +15 | ETH | DOWN | 0.63 | 0.81 | 1.54 |
| 10-09 10:16 | +10 | ETH | DOWN | 0.63 | 0.75 | 0.91 |
| 10-09 10:16 | +5 | ETH | DOWN | 0.63 | 0.68 | 0.19 |
| 10-09 10:16 | +10 stop | SOL | DOWN | 0.71 | 0.84 | 1.05 |
| 10-09 10:16 | +20 | SOL | DOWN | 0.71 | 0.93 | 1.96 |
| 10-09 10:16 | +15 | SOL | DOWN | 0.71 | 0.86 | 1.26 |
| 10-09 10:16 | +10 | SOL | DOWN | 0.71 | 0.84 | 1.05 |
| 10-09 10:16 | +5 | SOL | DOWN | 0.71 | 0.77 | 0.32 |
| 10-09 10:16 | +10 stop | ZEC | DOWN | 0.64 | 0.77 | 0.98 |
| 10-09 10:16 | +20 | ZEC | DOWN | 0.64 | open |  |
| 10-09 10:16 | +15 | ZEC | DOWN | 0.64 | 0.81 | 1.40 |
| 10-09 10:16 | +10 | ZEC | DOWN | 0.64 | 0.77 | 0.98 |
| 10-09 10:16 | +5 | ZEC | DOWN | 0.65 | 0.70 | 0.19 |
| 10-09 10:16 | +10 stop | BTC | DOWN | 0.61 | 0.76 | 1.20 |
| 10-09 10:16 | +20 | BTC | DOWN | 0.61 | 0.84 | 2.03 |
| 10-09 10:16 | +15 | BTC | DOWN | 0.61 | 0.76 | 1.20 |
| 10-09 10:16 | +10 | BTC | DOWN | 0.61 | 0.76 | 1.20 |
| 10-09 10:16 | +5 | BTC | DOWN | 0.61 | 0.68 | 0.37 |
| 10-09 10:16 | +10 stop | HYPE | DOWN | 0.56 | 0.69 | 0.97 |
| 10-09 10:16 | +20 | HYPE | DOWN | 0.56 | 0.76 | 1.69 |
| 10-09 10:16 | +15 | HYPE | DOWN | 0.56 | 0.76 | 1.69 |
| 10-09 10:16 | +10 | HYPE | DOWN | 0.56 | 0.69 | 0.97 |
| 10-09 10:16 | +5 | HYPE | DOWN | 0.56 | 0.61 | 0.15 |
| 10-09 10:16 | +10 stop | DOGE | DOWN | 0.63 | 0.76 | 1.00 |
| 10-09 10:16 | +20 | DOGE | DOWN | 0.63 | 0.84 | 1.83 |
| 10-09 10:16 | +15 | DOGE | DOWN | 0.63 | 0.80 | 1.41 |
| 10-09 10:16 | +10 | DOGE | DOWN | 0.63 | 0.76 | 1.00 |
| 10-09 10:16 | +5 | DOGE | DOWN | 0.63 | 0.70 | 0.38 |
| 10-09 10:16 | +10 stop | XRP | DOWN | 0.59 | 0.71 | 0.86 |
| 10-09 10:16 | +20 | XRP | DOWN | 0.59 | 0.84 | 2.21 |
