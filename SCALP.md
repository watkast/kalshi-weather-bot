# Range-Scalp Bot

*Updated Thu Nov 05 07:31 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 48233 | 42016 | 6217 (73) | 0 | $-13810.32 | -4.5% |
| **+10¢** | 36018 | 28795 | 7223 (99) | 1 | $-12666.91 | -5.6% |
| **+15¢** | 30184 | 22407 | 7777 (127) | 1 | $-11566.45 | -6.1% |
| **+20¢** | 26814 | 18667 | 8147 (166) | 1 | $-10220.25 | -6.1% |
| **+10¢ (15¢ stop)** | 58761 | 58668 | 93 (56) | 1 | $-21812.83 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-05 07:30 | +10 stop | BNB | DOWN | 0.71 | open |  |
| 11-05 07:30 | +20 | BNB | DOWN | 0.69 | open |  |
| 11-05 07:30 | +15 | BNB | DOWN | 0.69 | open |  |
| 11-05 07:30 | +10 | BNB | DOWN | 0.69 | open |  |
| 11-05 07:30 | +5 | BNB | DOWN | 0.69 | 0.74 | 0.21 |
| 11-05 07:27 | +10 stop | XRP | UP | 0.70 | 0.81 | 0.84 |
| 11-05 07:26 | +10 stop | DOGE | UP | 0.68 | 0.88 | 1.76 |
| 11-05 07:26 | +10 | DOGE | UP | 0.68 | 0.88 | 1.76 |
| 11-05 07:26 | +5 | DOGE | UP | 0.68 | 0.74 | 0.30 |
| 11-05 07:26 | +10 stop | NEAR | UP | 0.64 | 0.86 | 1.94 |
| 11-05 07:26 | +10 | NEAR | UP | 0.64 | 0.86 | 1.94 |
| 11-05 07:26 | +5 | NEAR | UP | 0.64 | 0.72 | 0.48 |
| 11-05 07:25 | +10 stop | DOGE | DOWN | 0.44 | 0.59 | 1.15 |
| 11-05 07:25 | +10 | DOGE | DOWN | 0.44 | 0.59 | 1.15 |
| 11-05 07:25 | +5 | DOGE | DOWN | 0.44 | 0.59 | 1.15 |
| 11-05 07:25 | +10 stop | ZEC | UP | 0.70 | 0.50 | -2.33 |
| 11-05 07:25 | +15 | ZEC | UP | 0.70 | 0.87 | 1.47 |
| 11-05 07:25 | +10 | ZEC | UP | 0.71 | 0.84 | 1.05 |
| 11-05 07:25 | +5 | ZEC | UP | 0.71 | 0.84 | 1.05 |
| 11-05 07:25 | +10 stop | HYPE | UP | 0.53 | 0.72 | 1.57 |
| 11-05 07:25 | +5 | HYPE | UP | 0.53 | 0.72 | 1.57 |
| 11-05 07:25 | +10 stop | NEAR | UP | 0.48 | 0.62 | 1.05 |
| 11-05 07:25 | +15 | NEAR | UP | 0.48 | 0.72 | 2.07 |
| 11-05 07:25 | +10 | NEAR | UP | 0.48 | 0.62 | 1.05 |
| 11-05 07:25 | +5 | NEAR | UP | 0.48 | 0.62 | 1.05 |
| 11-05 07:25 | +10 stop | DOGE | UP | 0.38 | 0.57 | 1.54 |
| 11-05 07:25 | +10 | DOGE | UP | 0.38 | 0.57 | 1.54 |
| 11-05 07:25 | +5 | DOGE | UP | 0.38 | 0.57 | 1.55 |
| 11-05 07:24 | +10 stop | HYPE | UP | 0.71 | 0.50 | -2.43 |
| 11-05 07:24 | +10 stop | BTC | DOWN | 0.63 | 0.73 | 0.69 |
| 11-05 07:24 | +20 | BTC | DOWN | 0.63 | 0.90 | 2.46 |
| 11-05 07:24 | +15 | BTC | DOWN | 0.63 | 0.90 | 2.46 |
| 11-05 07:24 | +10 | BTC | DOWN | 0.63 | 0.73 | 0.69 |
| 11-05 07:24 | +5 | BTC | DOWN | 0.63 | 0.71 | 0.48 |
| 11-05 07:24 | +10 stop | SOL | DOWN | 0.65 | 0.82 | 1.43 |
| 11-05 07:24 | +20 | SOL | DOWN | 0.65 | 0.85 | 1.75 |
| 11-05 07:24 | +15 | SOL | DOWN | 0.65 | 0.82 | 1.43 |
| 11-05 07:24 | +10 | SOL | DOWN | 0.65 | 0.82 | 1.43 |
| 11-05 07:24 | +5 | SOL | DOWN | 0.65 | 0.82 | 1.43 |
| 11-05 07:23 | +10 stop | HYPE | UP | 0.69 | 0.54 | -1.83 |
