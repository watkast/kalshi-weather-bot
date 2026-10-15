# Range-Scalp Bot

*Updated Thu Oct 15 03:09 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 16985 | 14739 | 2246 (28) | 0 | $-5222.35 | -4.9% |
| **+10¢** | 12845 | 10242 | 2603 (40) | 1 | $-4740.11 | -5.9% |
| **+15¢** | 10788 | 7990 | 2798 (59) | 1 | $-4243.59 | -6.3% |
| **+20¢** | 9584 | 6654 | 2930 (76) | 2 | $-3727.03 | -6.2% |
| **+10¢ (15¢ stop)** | 20895 | 20845 | 50 (29) | 0 | $-8070.89 | -6.2% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-15 03:08 | +10 stop | HYPE | DOWN | 0.69 | 0.54 | -1.83 |
| 10-15 03:08 | +10 | HYPE | DOWN | 0.69 | open |  |
| 10-15 03:08 | +5 | HYPE | DOWN | 0.69 | 0.76 | 0.42 |
| 10-15 03:01 | +10 stop | NEAR | DOWN | 0.67 | 0.77 | 0.71 |
| 10-15 03:01 | +20 | NEAR | DOWN | 0.67 | open |  |
| 10-15 03:01 | +15 | NEAR | DOWN | 0.66 | 0.82 | 1.33 |
| 10-15 03:01 | +10 | NEAR | DOWN | 0.66 | 0.77 | 0.81 |
| 10-15 03:01 | +5 | NEAR | DOWN | 0.66 | 0.77 | 0.81 |
| 10-15 03:01 | +10 stop | HYPE | DOWN | 0.70 | 0.82 | 0.94 |
| 10-15 03:01 | +20 | HYPE | DOWN | 0.70 | open |  |
| 10-15 03:01 | +15 | HYPE | DOWN | 0.70 | open |  |
| 10-15 03:01 | +10 | HYPE | DOWN | 0.70 | 0.82 | 0.94 |
| 10-15 03:01 | +5 | HYPE | DOWN | 0.70 | 0.78 | 0.52 |
| 10-15 03:01 | +10 stop | XRP | DOWN | 0.66 | 0.79 | 1.02 |
| 10-15 03:01 | +20 | XRP | DOWN | 0.66 | 0.86 | 1.75 |
| 10-15 03:01 | +15 | XRP | DOWN | 0.66 | 0.86 | 1.75 |
| 10-15 03:01 | +10 | XRP | DOWN | 0.66 | 0.79 | 1.01 |
| 10-15 03:01 | +5 | XRP | DOWN | 0.66 | 0.73 | 0.39 |
| 10-15 03:01 | +10 stop | DOGE | DOWN | 0.68 | 0.82 | 1.13 |
| 10-15 03:01 | +20 | DOGE | DOWN | 0.68 | 0.89 | 1.87 |
| 10-15 03:01 | +15 | DOGE | DOWN | 0.68 | 0.86 | 1.55 |
| 10-15 03:01 | +10 | DOGE | DOWN | 0.68 | 0.82 | 1.13 |
| 10-15 03:01 | +5 | DOGE | DOWN | 0.67 | 0.74 | 0.40 |
| 10-15 03:01 | +10 stop | ETH | DOWN | 0.65 | 0.77 | 0.91 |
| 10-15 03:01 | +20 | ETH | DOWN | 0.65 | 0.85 | 1.75 |
| 10-15 03:01 | +15 | ETH | DOWN | 0.65 | 0.81 | 1.33 |
| 10-15 03:01 | +10 | ETH | DOWN | 0.65 | 0.77 | 0.91 |
| 10-15 03:01 | +5 | ETH | DOWN | 0.65 | 0.77 | 0.91 |
| 10-15 03:01 | +10 stop | BNB | DOWN | 0.66 | 0.82 | 1.33 |
| 10-15 03:01 | +20 | BNB | DOWN | 0.66 | 0.87 | 1.86 |
| 10-15 03:01 | +15 | BNB | DOWN | 0.66 | 0.82 | 1.33 |
| 10-15 03:01 | +10 | BNB | DOWN | 0.66 | 0.82 | 1.33 |
| 10-15 03:01 | +5 | BNB | DOWN | 0.66 | 0.74 | 0.50 |
| 10-15 02:57 | +10 stop | HYPE | DOWN | 0.69 | 0.90 | 1.91 |
| 10-15 02:57 | +10 | HYPE | DOWN | 0.67 | 0.78 | 0.81 |
| 10-15 02:57 | +5 | HYPE | DOWN | 0.63 | 0.71 | 0.48 |
| 10-15 02:56 | +10 stop | NEAR | DOWN | 0.67 | 0.79 | 0.92 |
| 10-15 02:56 | +20 | NEAR | DOWN | 0.70 | 0.97 | 2.49 |
| 10-15 02:56 | +15 | NEAR | DOWN | 0.70 | 0.97 | 2.49 |
| 10-15 02:56 | +10 | NEAR | DOWN | 0.70 | 0.97 | 2.49 |
