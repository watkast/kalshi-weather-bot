# Range-Scalp Bot

*Updated Wed Oct 07 04:46 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 5964 | 5171 | 793 (9) | 1 | $-1828.17 | -4.9% |
| **+10¢** | 4550 | 3616 | 934 (16) | 1 | $-1720.38 | -6.0% |
| **+15¢** | 3823 | 2833 | 990 (20) | 1 | $-1489.87 | -6.2% |
| **+20¢** | 3412 | 2377 | 1035 (27) | 1 | $-1245.63 | -5.8% |
| **+10¢ (15¢ stop)** | 7244 | 7229 | 15 (9) | 1 | $-2524.32 | -5.6% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-07 04:45 | +10 stop | BNB | UP | 0.63 | open |  |
| 10-07 04:45 | +20 | BNB | UP | 0.63 | open |  |
| 10-07 04:45 | +15 | BNB | UP | 0.63 | open |  |
| 10-07 04:45 | +10 | BNB | UP | 0.63 | open |  |
| 10-07 04:45 | +5 | BNB | UP | 0.63 | open |  |
| 10-07 04:42 | +10 stop | ETH | DOWN | 0.56 | 0.79 | 2.00 |
| 10-07 04:42 | +15 | ETH | DOWN | 0.56 | 0.79 | 2.00 |
| 10-07 04:42 | +10 | ETH | DOWN | 0.56 | 0.79 | 2.00 |
| 10-07 04:42 | +5 | ETH | DOWN | 0.56 | 0.79 | 2.00 |
| 10-07 04:38 | +10 stop | ETH | UP | 0.61 | 0.72 | 0.78 |
| 10-07 04:38 | +15 | ETH | UP | 0.61 | 0.76 | 1.20 |
| 10-07 04:38 | +10 | ETH | UP | 0.61 | 0.72 | 0.78 |
| 10-07 04:38 | +5 | ETH | UP | 0.61 | 0.72 | 0.78 |
| 10-07 04:38 | +10 stop | BTC | DOWN | 0.67 | 0.77 | 0.71 |
| 10-07 04:38 | +5 | BTC | DOWN | 0.67 | 0.72 | 0.19 |
| 10-07 04:38 | +10 stop | ETH | DOWN | 0.42 | 0.58 | 1.24 |
| 10-07 04:38 | +15 | ETH | DOWN | 0.42 | 0.58 | 1.24 |
| 10-07 04:38 | +10 | ETH | DOWN | 0.42 | 0.58 | 1.24 |
| 10-07 04:38 | +5 | ETH | DOWN | 0.42 | 0.58 | 1.24 |
| 10-07 04:37 | +10 stop | BTC | DOWN | 0.65 | 0.76 | 0.81 |
| 10-07 04:37 | +15 | BTC | DOWN | 0.65 | 0.83 | 1.54 |
| 10-07 04:37 | +10 | BTC | DOWN | 0.67 | 0.77 | 0.71 |
| 10-07 04:37 | +5 | BTC | DOWN | 0.69 | 0.76 | 0.42 |
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
| 10-07 04:31 | +20 | ETH | DOWN | 0.68 | 0.91 | 2.12 |
| 10-07 04:31 | +15 | ETH | DOWN | 0.68 | 0.84 | 1.34 |
| 10-07 04:31 | +10 | ETH | DOWN | 0.68 | 0.79 | 0.82 |
| 10-07 04:31 | +5 | ETH | DOWN | 0.68 | 0.75 | 0.40 |
