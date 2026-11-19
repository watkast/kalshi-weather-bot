# Range-Scalp Bot

*Updated Thu Nov 19 06:09 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 64859 | 56601 | 8258 (124) | 1 | $-17483.71 | -4.3% |
| **+10¢** | 48451 | 38792 | 9659 (165) | 2 | $-16266.85 | -5.3% |
| **+15¢** | 40631 | 30215 | 10416 (210) | 2 | $-14672.32 | -5.8% |
| **+20¢** | 36181 | 25243 | 10938 (265) | 2 | $-12976.69 | -5.7% |
| **+10¢ (15¢ stop)** | 78911 | 78747 | 164 (98) | 1 | $-28971.80 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-19 06:08 | +10 stop | DOGE | UP | 0.65 | open |  |
| 11-19 06:08 | +20 | DOGE | UP | 0.64 | open |  |
| 11-19 06:08 | +15 | DOGE | UP | 0.64 | open |  |
| 11-19 06:08 | +10 | DOGE | UP | 0.64 | open |  |
| 11-19 06:08 | +5 | DOGE | UP | 0.64 | 0.69 | 0.18 |
| 11-19 06:06 | +10 stop | HYPE | DOWN | 0.64 | 0.74 | 0.69 |
| 11-19 06:05 | +10 stop | HYPE | UP | 0.53 | 0.37 | -1.95 |
| 11-19 06:05 | +20 | HYPE | UP | 0.53 | open |  |
| 11-19 06:05 | +15 | HYPE | UP | 0.53 | open |  |
| 11-19 06:05 | +10 | HYPE | UP | 0.53 | open |  |
| 11-19 06:05 | +5 | HYPE | UP | 0.53 | open |  |
| 11-19 06:01 | +10 stop | HYPE | UP | 0.70 | 0.83 | 1.05 |
| 11-19 06:01 | +20 | HYPE | UP | 0.70 | 0.90 | 1.78 |
| 11-19 06:01 | +15 | HYPE | UP | 0.70 | 0.89 | 1.68 |
| 11-19 06:01 | +10 | HYPE | UP | 0.70 | 0.83 | 1.05 |
| 11-19 06:01 | +5 | HYPE | UP | 0.70 | 0.75 | 0.21 |
| 11-19 06:00 | +10 stop | SOL | UP | 0.67 | 0.79 | 0.92 |
| 11-19 06:00 | +20 | SOL | UP | 0.67 | 0.92 | 2.26 |
| 11-19 06:00 | +15 | SOL | UP | 0.67 | 0.83 | 1.34 |
| 11-19 06:00 | +10 | SOL | UP | 0.68 | 0.79 | 0.82 |
| 11-19 06:00 | +5 | SOL | UP | 0.68 | 0.73 | 0.20 |
| 11-19 06:00 | +10 stop | ZEC | UP | 0.66 | 0.77 | 0.81 |
| 11-19 06:00 | +20 | ZEC | UP | 0.66 | 0.88 | 1.96 |
| 11-19 06:00 | +15 | ZEC | UP | 0.65 | 0.83 | 1.54 |
| 11-19 06:00 | +10 | ZEC | UP | 0.66 | 0.77 | 0.81 |
| 11-19 06:00 | +5 | ZEC | UP | 0.66 | 0.73 | 0.40 |
| 11-19 05:57 | +10 stop | ETH | UP | 0.65 | 0.47 | -2.14 |
| 11-19 05:56 | +10 stop | BTC | DOWN | 0.59 | 0.42 | -2.05 |
| 11-19 05:56 | +5 | BTC | DOWN | 0.59 | 0.64 | 0.16 |
| 11-19 05:55 | +10 stop | BTC | DOWN | 0.45 | 0.57 | 0.84 |
| 11-19 05:55 | +5 | BTC | DOWN | 0.45 | 0.57 | 0.84 |
| 11-19 05:55 | +10 stop | NEAR | UP | 0.65 | 0.81 | 1.36 |
| 11-19 05:55 | +10 | NEAR | UP | 0.65 | 0.81 | 1.32 |
| 11-19 05:55 | +5 | NEAR | UP | 0.65 | 0.81 | 1.32 |
| 11-19 05:54 | +10 stop | ETH | UP | 0.54 | 0.66 | 0.86 |
| 11-19 05:53 | +10 stop | ZEC | UP | 0.62 | 0.84 | 1.93 |
| 11-19 05:53 | +5 | ZEC | UP | 0.62 | 0.84 | 1.93 |
| 11-19 05:53 | +15 | DOGE | UP | 0.66 | 0.82 | 1.37 |
| 11-19 05:53 | +10 stop | DOGE | UP | 0.66 | 0.79 | 1.02 |
| 11-19 05:53 | +10 stop | BNB | DOWN | 0.62 | 0.23 | -4.20 |
