# Range-Scalp Bot

*Updated Sat Nov 07 12:16 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 50996 | 44456 | 6540 (76) | 0 | $-14293.78 | -4.5% |
| **+10¢** | 38072 | 30451 | 7621 (102) | 0 | $-13258.32 | -5.5% |
| **+15¢** | 31866 | 23651 | 8215 (131) | 0 | $-12203.67 | -6.1% |
| **+20¢** | 28336 | 19725 | 8611 (173) | 0 | $-10789.40 | -6.1% |
| **+10¢ (15¢ stop)** | 62103 | 62004 | 99 (58) | 0 | $-22920.88 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-07 12:12 | +10 stop | HYPE | UP | 0.66 | 0.76 | 0.71 |
| 11-07 12:10 | +10 stop | BNB | DOWN | 0.64 | 0.78 | 1.10 |
| 11-07 12:10 | +10 | BNB | DOWN | 0.67 | 0.78 | 0.81 |
| 11-07 12:10 | +5 | BNB | DOWN | 0.67 | 0.78 | 0.81 |
| 11-07 12:10 | +10 stop | HYPE | DOWN | 0.53 | 0.36 | -2.05 |
| 11-07 12:08 | +5 | BTC | UP | 0.71 | 0.78 | 0.42 |
| 11-07 12:08 | +10 stop | HYPE | UP | 0.49 | 0.61 | 0.85 |
| 11-07 12:07 | +5 | HYPE | UP | 0.61 | 0.74 | 0.99 |
| 11-07 12:07 | +10 stop | ZEC | DOWN | 0.69 | 0.83 | 1.15 |
| 11-07 12:07 | +10 stop | BNB | DOWN | 0.64 | 0.78 | 1.10 |
| 11-07 12:07 | +15 | BNB | DOWN | 0.64 | 0.98 | 3.17 |
| 11-07 12:07 | +10 | BNB | DOWN | 0.64 | 0.78 | 1.10 |
| 11-07 12:07 | +5 | BNB | DOWN | 0.64 | 0.78 | 1.10 |
| 11-07 12:06 | +5 | HYPE | DOWN | 0.59 | 0.64 | 0.16 |
| 11-07 12:06 | +10 stop | SOL | DOWN | 0.68 | 0.47 | -2.44 |
| 11-07 12:06 | +15 | SOL | DOWN | 0.68 | 0.91 | 2.06 |
| 11-07 12:06 | +10 | SOL | DOWN | 0.68 | 0.91 | 2.06 |
| 11-07 12:06 | +5 | SOL | DOWN | 0.68 | 0.91 | 2.06 |
| 11-07 12:05 | +10 stop | BTC | UP | 0.64 | 0.74 | 0.69 |
| 11-07 12:05 | +10 | BTC | UP | 0.64 | 0.74 | 0.69 |
| 11-07 12:05 | +5 | BTC | UP | 0.64 | 0.71 | 0.38 |
| 11-07 12:05 | +5 | BNB | DOWN | 0.70 | 0.77 | 0.42 |
| 11-07 12:05 | +10 stop | SOL | DOWN | 0.57 | 0.67 | 0.66 |
| 11-07 12:05 | +10 | SOL | DOWN | 0.57 | 0.67 | 0.66 |
| 11-07 12:05 | +5 | SOL | DOWN | 0.57 | 0.67 | 0.66 |
| 11-07 12:05 | +10 stop | ETH | DOWN | 0.59 | 0.70 | 0.78 |
| 11-07 12:05 | +10 | ETH | DOWN | 0.59 | 0.70 | 0.78 |
| 11-07 12:05 | +5 | ETH | DOWN | 0.59 | 0.70 | 0.78 |
| 11-07 12:04 | +5 | BNB | DOWN | 0.50 | 0.61 | 0.75 |
| 11-07 12:04 | +10 stop | BTC | UP | 0.58 | 0.72 | 1.07 |
| 11-07 12:04 | +10 stop | HYPE | DOWN | 0.58 | 0.39 | -2.25 |
| 11-07 12:04 | +10 | HYPE | DOWN | 0.58 | yes | -5.98 |
| 11-07 12:04 | +5 | HYPE | DOWN | 0.58 | 0.67 | 0.56 |
| 11-07 12:03 | +10 stop | BNB | DOWN | 0.63 | 0.77 | 1.10 |
| 11-07 12:03 | +20 | BNB | DOWN | 0.63 | 0.98 | 3.27 |
| 11-07 12:03 | +15 | BNB | DOWN | 0.63 | 0.80 | 1.41 |
| 11-07 12:03 | +10 | BNB | DOWN | 0.63 | 0.77 | 1.10 |
| 11-07 12:03 | +5 | BNB | DOWN | 0.63 | 0.71 | 0.48 |
| 11-07 12:03 | +10 stop | SOL | DOWN | 0.52 | 0.62 | 0.65 |
| 11-07 12:03 | +20 | SOL | DOWN | 0.52 | 0.91 | 3.64 |
