# Range-Scalp Bot

*Updated Wed Oct 07 04:36 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 5959 | 5166 | 793 (9) | 0 | $-1832.80 | -4.9% |
| **+10¢** | 4546 | 3612 | 934 (16) | 0 | $-1725.11 | -6.0% |
| **+15¢** | 3819 | 2829 | 990 (20) | 0 | $-1495.85 | -6.2% |
| **+20¢** | 3410 | 2375 | 1035 (27) | 2 | $-1249.71 | -5.8% |
| **+10¢ (15¢ stop)** | 7239 | 7224 | 15 (9) | 0 | $-2529.86 | -5.6% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-07 04:32 | +10 stop | DOGE | DOWN | 0.65 | 0.80 | 1.22 |
| 10-07 04:32 | +20 | DOGE | DOWN | 0.65 | 0.86 | 1.85 |
| 10-07 04:32 | +15 | DOGE | DOWN | 0.65 | 0.80 | 1.22 |
| 10-07 04:32 | +10 | DOGE | DOWN | 0.65 | 0.80 | 1.22 |
| 10-07 04:32 | +5 | DOGE | DOWN | 0.65 | 0.73 | 0.50 |
| 10-07 04:31 | +10 stop | BNB | DOWN | 0.66 | 0.81 | 1.23 |
| 10-07 04:31 | +20 | BNB | DOWN | 0.66 | 0.87 | 1.86 |
| 10-07 04:31 | +15 | BNB | DOWN | 0.66 | 0.81 | 1.23 |
| 10-07 04:31 | +10 | BNB | DOWN | 0.66 | 0.81 | 1.23 |
| 10-07 04:31 | +5 | BNB | DOWN | 0.66 | 0.74 | 0.50 |
| 10-07 04:31 | +10 stop | ZEC | DOWN | 0.69 | 0.83 | 1.15 |
| 10-07 04:31 | +20 | ZEC | DOWN | 0.69 | 0.90 | 1.88 |
| 10-07 04:31 | +10 stop | ETH | DOWN | 0.68 | 0.79 | 0.82 |
| 10-07 04:31 | +20 | ETH | DOWN | 0.68 | open |  |
| 10-07 04:31 | +15 | ETH | DOWN | 0.68 | 0.84 | 1.34 |
| 10-07 04:31 | +10 | ETH | DOWN | 0.68 | 0.79 | 0.82 |
| 10-07 04:31 | +5 | ETH | DOWN | 0.68 | 0.75 | 0.40 |
| 10-07 04:31 | +10 stop | NEAR | DOWN | 0.67 | 0.79 | 0.93 |
| 10-07 04:31 | +20 | NEAR | DOWN | 0.67 | 0.89 | 1.98 |
| 10-07 04:31 | +15 | NEAR | DOWN | 0.67 | 0.84 | 1.45 |
| 10-07 04:31 | +10 | NEAR | DOWN | 0.67 | 0.79 | 0.93 |
| 10-07 04:31 | +5 | NEAR | DOWN | 0.67 | 0.74 | 0.41 |
| 10-07 04:31 | +15 | ZEC | DOWN | 0.69 | 0.86 | 1.46 |
| 10-07 04:31 | +10 | ZEC | DOWN | 0.69 | 0.83 | 1.15 |
| 10-07 04:31 | +5 | ZEC | DOWN | 0.69 | 0.83 | 1.15 |
| 10-07 04:31 | +10 stop | HYPE | DOWN | 0.64 | 0.77 | 1.00 |
| 10-07 04:31 | +20 | HYPE | DOWN | 0.64 | 0.91 | 2.41 |
| 10-07 04:31 | +15 | HYPE | DOWN | 0.64 | 0.79 | 1.21 |
| 10-07 04:31 | +10 | HYPE | DOWN | 0.64 | 0.77 | 1.00 |
| 10-07 04:31 | +5 | HYPE | DOWN | 0.64 | 0.72 | 0.48 |
| 10-07 04:31 | +10 stop | XRP | DOWN | 0.67 | 0.85 | 1.55 |
| 10-07 04:31 | +20 | XRP | DOWN | 0.67 | 0.88 | 1.86 |
| 10-07 04:31 | +15 | XRP | DOWN | 0.67 | 0.85 | 1.55 |
| 10-07 04:31 | +10 | XRP | DOWN | 0.69 | 0.85 | 1.36 |
| 10-07 04:31 | +5 | XRP | DOWN | 0.69 | 0.76 | 0.42 |
| 10-07 04:31 | +10 stop | BTC | DOWN | 0.66 | 0.80 | 1.12 |
| 10-07 04:31 | +20 | BTC | DOWN | 0.66 | open |  |
| 10-07 04:31 | +15 | BTC | DOWN | 0.66 | 0.81 | 1.23 |
| 10-07 04:31 | +10 | BTC | DOWN | 0.66 | 0.80 | 1.12 |
| 10-07 04:31 | +5 | BTC | DOWN | 0.67 | 0.73 | 0.30 |
