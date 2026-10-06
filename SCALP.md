# Range-Scalp Bot

*Updated Tue Oct 06 23:35 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 5637 | 4885 | 752 (9) | 1 | $-1729.40 | -4.9% |
| **+10¢** | 4299 | 3412 | 887 (15) | 2 | $-1664.22 | -6.2% |
| **+15¢** | 3606 | 2666 | 940 (19) | 2 | $-1456.24 | -6.4% |
| **+20¢** | 3222 | 2245 | 977 (26) | 3 | $-1177.72 | -5.8% |
| **+10¢ (15¢ stop)** | 6870 | 6855 | 15 (9) | 0 | $-2476.76 | -5.7% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-06 23:35 | +5 | DOGE | DOWN | 0.50 | 0.57 | 0.34 |
| 10-06 23:35 | +5 | DOGE | DOWN | 0.58 | 0.64 | 0.25 |
| 10-06 23:34 | +10 stop | DOGE | DOWN | 0.65 | 0.50 | -1.84 |
| 10-06 23:33 | +10 stop | ZEC | DOWN | 0.66 | 0.79 | 1.00 |
| 10-06 23:33 | +10 stop | DOGE | DOWN | 0.59 | 0.44 | -1.85 |
| 10-06 23:33 | +5 | DOGE | DOWN | 0.57 | 0.63 | 0.23 |
| 10-06 23:32 | +5 | HYPE | DOWN | 0.71 | 0.79 | 0.53 |
| 10-06 23:32 | +10 | BNB | DOWN | 0.68 | 0.84 | 1.34 |
| 10-06 23:32 | +5 | BNB | DOWN | 0.68 | 0.76 | 0.51 |
| 10-06 23:32 | +10 stop | BNB | DOWN | 0.70 | 0.84 | 1.15 |
| 10-06 23:32 | +20 | BNB | DOWN | 0.70 | open |  |
| 10-06 23:32 | +15 | BNB | DOWN | 0.69 | 0.84 | 1.25 |
| 10-06 23:32 | +10 stop | ZEC | DOWN | 0.59 | 0.69 | 0.68 |
| 10-06 23:32 | +5 | DOGE | UP | 0.55 | 0.62 | 0.35 |
| 10-06 23:32 | +5 | HYPE | DOWN | 0.53 | 0.63 | 0.61 |
| 10-06 23:31 | +10 stop | DOGE | UP | 0.55 | 0.39 | -1.95 |
| 10-06 23:31 | +20 | DOGE | UP | 0.55 | open |  |
| 10-06 23:31 | +15 | DOGE | UP | 0.55 | open |  |
| 10-06 23:31 | +10 | DOGE | UP | 0.55 | open |  |
| 10-06 23:31 | +5 | DOGE | UP | 0.55 | 0.62 | 0.35 |
| 10-06 23:31 | +10 stop | HYPE | DOWN | 0.58 | 0.68 | 0.66 |
| 10-06 23:31 | +20 | HYPE | DOWN | 0.58 | 0.79 | 1.80 |
| 10-06 23:31 | +15 | HYPE | DOWN | 0.58 | 0.73 | 1.18 |
| 10-06 23:31 | +10 | HYPE | DOWN | 0.58 | 0.68 | 0.66 |
| 10-06 23:31 | +5 | HYPE | DOWN | 0.58 | 0.63 | 0.15 |
| 10-06 23:31 | +10 stop | ZEC | UP | 0.65 | 0.32 | -3.62 |
| 10-06 23:31 | +20 | ZEC | UP | 0.65 | open |  |
| 10-06 23:31 | +15 | ZEC | UP | 0.65 | open |  |
| 10-06 23:31 | +10 | ZEC | UP | 0.65 | open |  |
| 10-06 23:31 | +5 | ZEC | UP | 0.65 | open |  |
| 10-06 23:31 | +10 stop | ETH | DOWN | 0.56 | 0.71 | 1.17 |
| 10-06 23:31 | +20 | ETH | DOWN | 0.56 | 0.83 | 2.42 |
| 10-06 23:31 | +15 | ETH | DOWN | 0.56 | 0.71 | 1.17 |
| 10-06 23:31 | +10 | ETH | DOWN | 0.56 | 0.71 | 1.17 |
| 10-06 23:31 | +5 | ETH | DOWN | 0.56 | 0.71 | 1.17 |
| 10-06 23:31 | +10 stop | BTC | DOWN | 0.59 | 0.76 | 1.40 |
| 10-06 23:31 | +20 | BTC | DOWN | 0.59 | 0.81 | 1.92 |
| 10-06 23:31 | +15 | BTC | DOWN | 0.59 | 0.76 | 1.40 |
| 10-06 23:31 | +10 | BTC | DOWN | 0.59 | 0.76 | 1.40 |
| 10-06 23:31 | +5 | BTC | DOWN | 0.59 | 0.66 | 0.37 |
