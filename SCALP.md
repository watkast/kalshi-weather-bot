# Range-Scalp Bot

*Updated Thu Nov 12 01:53 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 56415 | 49189 | 7226 (98) | 9 | $-15459.38 | -4.4% |
| **+10¢** | 42161 | 33731 | 8430 (128) | 9 | $-14408.49 | -5.4% |
| **+15¢** | 35355 | 26271 | 9084 (162) | 9 | $-13099.77 | -5.9% |
| **+20¢** | 31496 | 21966 | 9530 (212) | 9 | $-11452.77 | -5.8% |
| **+10¢ (15¢ stop)** | 68763 | 68640 | 123 (73) | 3 | $-25370.20 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-12 01:52 | +10 stop | ZEC | DOWN | 0.66 | open |  |
| 11-12 01:52 | +10 stop | BTC | DOWN | 0.63 | open |  |
| 11-12 01:52 | +10 stop | HYPE | DOWN | 0.70 | open |  |
| 11-12 01:51 | +10 stop | ZEC | DOWN | 0.53 | 0.65 | 0.86 |
| 11-12 01:51 | +10 stop | HYPE | DOWN | 0.70 | 0.54 | -1.91 |
| 11-12 01:51 | +10 stop | NEAR | DOWN | 0.69 | 0.53 | -1.93 |
| 11-12 01:51 | +10 stop | ETH | DOWN | 0.62 | 0.76 | 1.10 |
| 11-12 01:50 | +10 stop | BTC | DOWN | 0.68 | 0.53 | -1.84 |
| 11-12 01:50 | +10 stop | ZEC | DOWN | 0.71 | 0.54 | -2.03 |
| 11-12 01:50 | +5 | ZEC | DOWN | 0.70 | open |  |
| 11-12 01:49 | +10 stop | NEAR | DOWN | 0.62 | 0.73 | 0.79 |
| 11-12 01:49 | +10 stop | HYPE | DOWN | 0.65 | 0.78 | 1.01 |
| 11-12 01:49 | +5 | ZEC | UP | 0.53 | 0.63 | 0.65 |
| 11-12 01:49 | +10 stop | SOL | DOWN | 0.61 | 0.73 | 0.89 |
| 11-12 01:48 | +10 stop | ETH | UP | 0.59 | 0.42 | -2.05 |
| 11-12 01:48 | +10 stop | BNB | DOWN | 0.48 | 0.71 | 1.97 |
| 11-12 01:48 | +10 stop | DOGE | DOWN | 0.69 | 0.83 | 1.15 |
| 11-12 01:48 | +10 stop | XRP | DOWN | 0.63 | 0.73 | 0.69 |
| 11-12 01:47 | +10 stop | DOGE | UP | 0.59 | 0.41 | -2.14 |
| 11-12 01:47 | +10 | DOGE | UP | 0.59 | open |  |
| 11-12 01:47 | +5 | DOGE | UP | 0.59 | open |  |
| 11-12 01:47 | +10 stop | XRP | UP | 0.58 | 0.42 | -1.95 |
| 11-12 01:47 | +20 | XRP | UP | 0.58 | open |  |
| 11-12 01:47 | +15 | XRP | UP | 0.57 | open |  |
| 11-12 01:47 | +10 | XRP | UP | 0.57 | open |  |
| 11-12 01:47 | +5 | XRP | UP | 0.58 | open |  |
| 11-12 01:47 | +10 stop | BNB | UP | 0.62 | 0.45 | -2.05 |
| 11-12 01:47 | +20 | BNB | UP | 0.62 | open |  |
| 11-12 01:47 | +15 | BNB | UP | 0.61 | open |  |
| 11-12 01:47 | +10 | BNB | UP | 0.61 | open |  |
| 11-12 01:47 | +5 | BNB | UP | 0.61 | open |  |
| 11-12 01:47 | +10 stop | BTC | UP | 0.66 | 0.44 | -2.54 |
| 11-12 01:47 | +20 | BTC | UP | 0.65 | open |  |
| 11-12 01:47 | +15 | BTC | UP | 0.65 | open |  |
| 11-12 01:47 | +10 | BTC | UP | 0.65 | open |  |
| 11-12 01:47 | +5 | BTC | UP | 0.65 | open |  |
| 11-12 01:47 | +10 stop | SOL | UP | 0.61 | 0.46 | -1.85 |
| 11-12 01:47 | +20 | SOL | UP | 0.61 | open |  |
| 11-12 01:47 | +15 | SOL | UP | 0.61 | open |  |
| 11-12 01:47 | +10 | SOL | UP | 0.61 | open |  |
