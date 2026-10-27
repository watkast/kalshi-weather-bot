# Range-Scalp Bot

*Updated Tue Oct 27 06:26 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 36103 | 31518 | 4585 (43) | 0 | $-10039.57 | -4.4% |
| **+10¢** | 26988 | 21684 | 5304 (65) | 1 | $-8875.12 | -5.2% |
| **+15¢** | 22587 | 16889 | 5698 (89) | 1 | $-7858.55 | -5.5% |
| **+20¢** | 20021 | 14051 | 5970 (112) | 1 | $-6897.69 | -5.5% |
| **+10¢ (15¢ stop)** | 44273 | 44210 | 63 (33) | 0 | $-16863.75 | -6.1% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 10-27 06:24 | +10 stop | HYPE | DOWN | 0.55 | 0.74 | 1.58 |
| 10-27 06:23 | +10 stop | HYPE | DOWN | 0.70 | 0.53 | -2.03 |
| 10-27 06:23 | +15 | HYPE | DOWN | 0.70 | open |  |
| 10-27 06:23 | +10 | HYPE | DOWN | 0.70 | open |  |
| 10-27 06:23 | +5 | HYPE | DOWN | 0.70 | 0.79 | 0.63 |
| 10-27 06:19 | +10 stop | HYPE | DOWN | 0.69 | 0.81 | 0.94 |
| 10-27 06:18 | +10 stop | DOGE | DOWN | 0.68 | 0.78 | 0.71 |
| 10-27 06:18 | +15 | DOGE | DOWN | 0.68 | 0.88 | 1.76 |
| 10-27 06:18 | +10 | DOGE | DOWN | 0.69 | 0.80 | 0.83 |
| 10-27 06:18 | +5 | DOGE | DOWN | 0.69 | 0.74 | 0.21 |
| 10-27 06:18 | +10 stop | SOL | DOWN | 0.64 | 0.76 | 0.90 |
| 10-27 06:18 | +20 | SOL | DOWN | 0.64 | 0.86 | 1.94 |
| 10-27 06:18 | +15 | SOL | DOWN | 0.64 | 0.86 | 1.94 |
| 10-27 06:18 | +10 | SOL | DOWN | 0.64 | 0.76 | 0.90 |
| 10-27 06:18 | +5 | SOL | DOWN | 0.64 | 0.71 | 0.38 |
| 10-27 06:16 | +10 stop | HYPE | DOWN | 0.69 | 0.54 | -1.83 |
| 10-27 06:16 | +20 | HYPE | DOWN | 0.69 | open |  |
| 10-27 06:16 | +15 | HYPE | DOWN | 0.69 | 0.84 | 1.25 |
| 10-27 06:16 | +10 | HYPE | DOWN | 0.69 | 0.81 | 0.94 |
| 10-27 06:16 | +5 | HYPE | DOWN | 0.69 | 0.76 | 0.42 |
| 10-27 06:16 | +10 stop | ZEC | DOWN | 0.68 | 0.86 | 1.55 |
| 10-27 06:16 | +20 | ZEC | DOWN | 0.68 | 0.89 | 1.87 |
| 10-27 06:16 | +15 | ZEC | DOWN | 0.68 | 0.86 | 1.55 |
| 10-27 06:16 | +10 | ZEC | DOWN | 0.68 | 0.86 | 1.55 |
| 10-27 06:16 | +5 | ZEC | DOWN | 0.68 | 0.73 | 0.20 |
| 10-27 06:16 | +5 | NEAR | DOWN | 0.70 | 0.76 | 0.32 |
| 10-27 06:16 | +10 stop | DOGE | DOWN | 0.64 | 0.74 | 0.69 |
| 10-27 06:16 | +20 | DOGE | DOWN | 0.64 | 0.88 | 2.15 |
| 10-27 06:16 | +15 | DOGE | DOWN | 0.64 | 0.79 | 1.21 |
| 10-27 06:16 | +10 | DOGE | DOWN | 0.64 | 0.74 | 0.69 |
| 10-27 06:16 | +5 | DOGE | DOWN | 0.64 | 0.74 | 0.69 |
| 10-27 06:16 | +10 stop | XRP | DOWN | 0.64 | 0.79 | 1.21 |
| 10-27 06:16 | +20 | XRP | DOWN | 0.64 | 0.86 | 1.94 |
| 10-27 06:16 | +15 | XRP | DOWN | 0.64 | 0.79 | 1.21 |
| 10-27 06:16 | +10 | XRP | DOWN | 0.64 | 0.79 | 1.21 |
| 10-27 06:16 | +5 | XRP | DOWN | 0.64 | 0.79 | 1.21 |
| 10-27 06:12 | +10 stop | XRP | DOWN | 0.67 | 0.83 | 1.34 |
| 10-27 06:12 | +15 | XRP | DOWN | 0.67 | 0.83 | 1.34 |
| 10-27 06:11 | +10 stop | ZEC | DOWN | 0.71 | 0.81 | 0.74 |
| 10-27 06:11 | +20 | ZEC | DOWN | 0.71 | 0.95 | 2.22 |
