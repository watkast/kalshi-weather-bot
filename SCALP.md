# Range-Scalp Bot

*Updated Tue Nov 03 18:37 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 46165 | 40197 | 5968 (72) | 1 | $-13293.52 | -4.6% |
| **+10¢** | 34460 | 27544 | 6916 (96) | 1 | $-12159.45 | -5.6% |
| **+15¢** | 28844 | 21410 | 7434 (124) | 1 | $-11079.04 | -6.1% |
| **+20¢** | 25624 | 17831 | 7793 (164) | 1 | $-9818.30 | -6.1% |
| **+10¢ (15¢ stop)** | 56322 | 56229 | 93 (56) | 0 | $-21124.99 | -6.0% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-03 18:31 | +10 stop | BNB | UP | 0.68 | 0.81 | 1.03 |
| 11-03 18:31 | +20 | BNB | UP | 0.68 | 0.88 | 1.76 |
| 11-03 18:31 | +15 | BNB | UP | 0.68 | 0.84 | 1.34 |
| 11-03 18:31 | +10 | BNB | UP | 0.68 | 0.81 | 1.03 |
| 11-03 18:31 | +5 | BNB | UP | 0.68 | 0.81 | 1.03 |
| 11-03 18:31 | +10 stop | ZEC | UP | 0.65 | 0.78 | 1.01 |
| 11-03 18:31 | +20 | ZEC | UP | 0.65 | 0.88 | 2.06 |
| 11-03 18:31 | +15 | ZEC | UP | 0.65 | 0.84 | 1.64 |
| 11-03 18:31 | +10 | ZEC | UP | 0.65 | 0.78 | 1.01 |
| 11-03 18:31 | +5 | ZEC | UP | 0.65 | 0.78 | 1.01 |
| 11-03 18:31 | +10 stop | XRP | DOWN | 0.56 | 0.39 | -2.05 |
| 11-03 18:31 | +20 | XRP | DOWN | 0.56 | open |  |
| 11-03 18:31 | +15 | XRP | DOWN | 0.56 | open |  |
| 11-03 18:31 | +10 | XRP | DOWN | 0.56 | open |  |
| 11-03 18:31 | +5 | XRP | DOWN | 0.56 | open |  |
| 11-03 18:24 | +10 stop | BTC | DOWN | 0.64 | 0.74 | 0.69 |
| 11-03 18:24 | +20 | BTC | DOWN | 0.64 | 0.87 | 2.05 |
| 11-03 18:24 | +15 | BTC | DOWN | 0.64 | 0.87 | 2.05 |
| 11-03 18:24 | +10 | BTC | DOWN | 0.64 | 0.74 | 0.69 |
| 11-03 18:24 | +5 | BTC | DOWN | 0.64 | 0.69 | 0.18 |
| 11-03 18:22 | +10 stop | HYPE | DOWN | 0.66 | 0.84 | 1.54 |
| 11-03 18:20 | +10 stop | SOL | DOWN | 0.66 | 0.78 | 0.91 |
| 11-03 18:20 | +20 | SOL | DOWN | 0.66 | 0.87 | 1.86 |
| 11-03 18:20 | +10 | SOL | DOWN | 0.65 | 0.78 | 1.01 |
| 11-03 18:20 | +5 | SOL | DOWN | 0.63 | 0.73 | 0.69 |
| 11-03 18:19 | +10 stop | SOL | DOWN | 0.69 | 0.79 | 0.73 |
| 11-03 18:19 | +15 | SOL | DOWN | 0.69 | 0.85 | 1.36 |
| 11-03 18:19 | +10 | SOL | DOWN | 0.69 | 0.79 | 0.73 |
| 11-03 18:19 | +5 | SOL | DOWN | 0.69 | 0.79 | 0.73 |
| 11-03 18:19 | +10 stop | ZEC | DOWN | 0.67 | 0.80 | 1.02 |
| 11-03 18:19 | +10 | ZEC | DOWN | 0.67 | 0.80 | 1.02 |
| 11-03 18:19 | +5 | ZEC | DOWN | 0.67 | 0.76 | 0.61 |
| 11-03 18:18 | +5 | BNB | DOWN | 0.65 | 0.73 | 0.54 |
| 11-03 18:17 | +10 stop | SOL | DOWN | 0.59 | 0.72 | 0.98 |
| 11-03 18:17 | +10 | SOL | DOWN | 0.59 | 0.72 | 0.98 |
| 11-03 18:17 | +10 stop | XRP | DOWN | 0.67 | 0.78 | 0.81 |
| 11-03 18:17 | +20 | XRP | DOWN | 0.67 | 0.87 | 1.76 |
| 11-03 18:17 | +15 | XRP | DOWN | 0.67 | 0.83 | 1.34 |
| 11-03 18:17 | +10 | XRP | DOWN | 0.67 | 0.78 | 0.81 |
| 11-03 18:17 | +5 | XRP | DOWN | 0.67 | 0.78 | 0.81 |
