# Range-Scalp Bot

*Updated Mon Nov 09 08:14 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 53535 | 46683 | 6852 (85) | 2 | $-14750.38 | -4.4% |
| **+10¢** | 39992 | 32001 | 7991 (110) | 3 | $-13739.00 | -5.5% |
| **+15¢** | 33507 | 24896 | 8611 (141) | 3 | $-12537.91 | -6.0% |
| **+20¢** | 29816 | 20785 | 9031 (186) | 4 | $-11035.35 | -5.9% |
| **+10¢ (15¢ stop)** | 65243 | 65137 | 106 (63) | 0 | $-24161.95 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-09 08:13 | +10 stop | BTC | DOWN | 0.63 | 0.43 | -2.35 |
| 11-09 08:13 | +5 | BTC | DOWN | 0.63 | open |  |
| 11-09 08:11 | +10 stop | BTC | UP | 0.57 | 0.42 | -1.86 |
| 11-09 08:11 | +20 | BTC | UP | 0.57 | open |  |
| 11-09 08:11 | +15 | BTC | UP | 0.57 | open |  |
| 11-09 08:11 | +10 | BTC | UP | 0.57 | open |  |
| 11-09 08:10 | +10 stop | ETH | UP | 0.70 | 0.47 | -2.63 |
| 11-09 08:10 | +10 stop | HYPE | UP | 0.63 | 0.44 | -2.25 |
| 11-09 08:10 | +10 stop | HYPE | DOWN | 0.39 | 0.52 | 0.95 |
| 11-09 08:09 | +10 stop | SOL | UP | 0.71 | 0.82 | 0.84 |
| 11-09 08:09 | +10 | SOL | UP | 0.71 | 0.82 | 0.84 |
| 11-09 08:09 | +5 | SOL | UP | 0.71 | 0.82 | 0.84 |
| 11-09 08:09 | +10 stop | HYPE | DOWN | 0.67 | 0.52 | -1.84 |
| 11-09 08:08 | +10 stop | BTC | UP | 0.68 | 0.50 | -2.14 |
| 11-09 08:08 | +10 stop | ETH | UP | 0.61 | 0.44 | -2.05 |
| 11-09 08:08 | +10 | ETH | UP | 0.61 | 0.74 | 0.99 |
| 11-09 08:08 | +10 stop | ZEC | DOWN | 0.61 | 0.73 | 0.89 |
| 11-09 08:08 | +10 stop | BTC | DOWN | 0.65 | 0.42 | -2.64 |
| 11-09 08:07 | +10 stop | HYPE | DOWN | 0.69 | 0.47 | -2.53 |
| 11-09 08:07 | +5 | HYPE | DOWN | 0.69 | 0.77 | 0.52 |
| 11-09 08:07 | +20 | SOL | UP | 0.62 | 0.82 | 1.72 |
| 11-09 08:07 | +15 | SOL | UP | 0.62 | 0.82 | 1.72 |
| 11-09 08:07 | +10 | SOL | UP | 0.62 | 0.72 | 0.68 |
| 11-09 08:07 | +5 | SOL | UP | 0.62 | 0.72 | 0.68 |
| 11-09 08:07 | +20 | XRP | UP | 0.57 | 0.77 | 1.71 |
| 11-09 08:07 | +15 | XRP | UP | 0.56 | 0.75 | 1.58 |
| 11-09 08:07 | +5 | XRP | UP | 0.56 | 0.75 | 1.58 |
| 11-09 08:07 | +10 stop | BTC | UP | 0.61 | 0.42 | -2.25 |
| 11-09 08:06 | +10 stop | ETH | UP | 0.65 | 0.50 | -1.84 |
| 11-09 08:06 | +10 stop | ZEC | UP | 0.60 | 0.32 | -3.13 |
| 11-09 08:06 | +5 | ZEC | UP | 0.59 | open |  |
| 11-09 08:05 | +10 stop | ETH | DOWN | 0.60 | 0.44 | -1.95 |
| 11-09 08:05 | +10 | SOL | UP | 0.63 | 0.74 | 0.79 |
| 11-09 08:04 | +10 stop | HYPE | UP | 0.57 | 0.75 | 1.48 |
| 11-09 08:04 | +5 | HYPE | UP | 0.61 | 0.75 | 1.11 |
| 11-09 08:04 | +5 | XRP | UP | 0.64 | 0.72 | 0.48 |
| 11-09 08:04 | +10 stop | SOL | UP | 0.66 | 0.76 | 0.71 |
| 11-09 08:04 | +5 | SOL | UP | 0.67 | 0.74 | 0.40 |
| 11-09 08:03 | +10 stop | NEAR | DOWN | 0.70 | 0.81 | 0.84 |
| 11-09 08:03 | +10 stop | XRP | UP | 0.67 | 0.50 | -2.04 |
