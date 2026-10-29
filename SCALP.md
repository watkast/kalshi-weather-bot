# Range-Scalp Bot

*Updated Thu Oct 29 04:08 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 38954 | 33989 | 4965 (49) | 0 | $-10968.51 | -4.5% |
| **+10¢** | 29062 | 23333 | 5729 (71) | 1 | $-9685.17 | -5.3% |
| **+15¢** | 24307 | 18151 | 6156 (97) | 1 | $-8653.42 | -5.7% |
| **+20¢** | 21567 | 15118 | 6449 (125) | 2 | $-7560.55 | -5.6% |
| **+10¢ (15¢ stop)** | 47637 | 47570 | 67 (35) | 0 | $-18075.47 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-29 04:06 | +10 stop | BNB | DOWN | 0.67 | 0.86 | 1.65 |
| 10-29 04:06 | +15 | BNB | DOWN | 0.67 | 0.86 | 1.65 |
| 10-29 04:06 | +10 | BNB | DOWN | 0.66 | 0.86 | 1.75 |
| 10-29 04:06 | +5 | BNB | DOWN | 0.66 | 0.86 | 1.75 |
| 10-29 04:06 | +10 stop | BTC | DOWN | 0.63 | 0.73 | 0.69 |
| 10-29 04:06 | +10 | BTC | DOWN | 0.63 | 0.73 | 0.69 |
| 10-29 04:06 | +5 | BTC | DOWN | 0.63 | 0.68 | 0.17 |
| 10-29 04:05 | +10 stop | HYPE | DOWN | 0.68 | 0.51 | -2.04 |
| 10-29 04:05 | +10 | HYPE | DOWN | 0.68 | open |  |
| 10-29 04:05 | +5 | HYPE | DOWN | 0.68 | 0.75 | 0.40 |
| 10-29 04:03 | +5 | NEAR | DOWN | 0.57 | 0.62 | 0.15 |
| 10-29 04:03 | +10 | BTC | DOWN | 0.63 | 0.73 | 0.69 |
| 10-29 04:01 | +5 | BTC | DOWN | 0.67 | 0.73 | 0.30 |
| 10-29 04:00 | +10 stop | BNB | DOWN | 0.64 | 0.77 | 1.00 |
| 10-29 04:00 | +20 | BNB | DOWN | 0.64 | 0.86 | 1.94 |
| 10-29 04:00 | +15 | BNB | DOWN | 0.64 | 0.80 | 1.31 |
| 10-29 04:00 | +10 | BNB | DOWN | 0.64 | 0.77 | 1.00 |
| 10-29 04:00 | +5 | BNB | DOWN | 0.64 | 0.77 | 1.00 |
| 10-29 04:00 | +10 stop | ZEC | DOWN | 0.65 | 0.75 | 0.70 |
| 10-29 04:00 | +20 | ZEC | DOWN | 0.64 | 0.84 | 1.73 |
| 10-29 04:00 | +15 | ZEC | DOWN | 0.64 | 0.79 | 1.21 |
| 10-29 04:00 | +10 | ZEC | DOWN | 0.64 | 0.75 | 0.79 |
| 10-29 04:00 | +5 | ZEC | DOWN | 0.64 | 0.69 | 0.18 |
| 10-29 04:00 | +10 stop | DOGE | DOWN | 0.64 | 0.77 | 1.00 |
| 10-29 04:00 | +20 | DOGE | DOWN | 0.64 | 0.88 | 2.15 |
| 10-29 04:00 | +15 | DOGE | DOWN | 0.64 | 0.79 | 1.21 |
| 10-29 04:00 | +10 | DOGE | DOWN | 0.64 | 0.77 | 1.00 |
| 10-29 04:00 | +5 | DOGE | DOWN | 0.64 | 0.70 | 0.28 |
| 10-29 04:00 | +10 stop | SOL | DOWN | 0.64 | 0.74 | 0.69 |
| 10-29 04:00 | +20 | SOL | DOWN | 0.63 | 0.86 | 2.01 |
| 10-29 04:00 | +15 | SOL | DOWN | 0.63 | 0.78 | 1.20 |
| 10-29 04:00 | +10 | SOL | DOWN | 0.63 | 0.74 | 0.79 |
| 10-29 04:00 | +5 | SOL | DOWN | 0.63 | 0.74 | 0.79 |
| 10-29 04:00 | +10 stop | BTC | DOWN | 0.62 | 0.73 | 0.79 |
| 10-29 04:00 | +20 | BTC | DOWN | 0.62 | open |  |
| 10-29 04:00 | +15 | BTC | DOWN | 0.61 | 0.80 | 1.61 |
| 10-29 04:00 | +10 | BTC | DOWN | 0.61 | 0.71 | 0.68 |
| 10-29 04:00 | +5 | BTC | DOWN | 0.61 | 0.69 | 0.48 |
| 10-29 04:00 | +10 stop | ETH | DOWN | 0.67 | 0.77 | 0.71 |
| 10-29 04:00 | +20 | ETH | DOWN | 0.67 | 0.91 | 2.17 |
