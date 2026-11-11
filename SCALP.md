# Range-Scalp Bot

*Updated Wed Nov 11 02:32 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 55271 | 48207 | 7064 (94) | 3 | $-15059.27 | -4.3% |
| **+10¢** | 41293 | 33052 | 8241 (124) | 4 | $-13992.27 | -5.4% |
| **+15¢** | 34618 | 25736 | 8882 (158) | 5 | $-12728.98 | -5.9% |
| **+20¢** | 30822 | 21504 | 9318 (207) | 5 | $-11128.93 | -5.8% |
| **+10¢ (15¢ stop)** | 67319 | 67201 | 118 (73) | 2 | $-24807.74 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-11 02:32 | +10 stop | ETH | UP | 0.67 | open |  |
| 11-11 02:32 | +20 | ETH | UP | 0.67 | open |  |
| 11-11 02:32 | +15 | ETH | UP | 0.69 | open |  |
| 11-11 02:32 | +10 | ETH | UP | 0.69 | open |  |
| 11-11 02:32 | +5 | ETH | UP | 0.69 | open |  |
| 11-11 02:32 | +5 | NEAR | UP | 0.68 | 0.81 | 1.03 |
| 11-11 02:31 | +10 stop | NEAR | UP | 0.60 | 0.71 | 0.78 |
| 11-11 02:31 | +10 | NEAR | UP | 0.60 | 0.71 | 0.78 |
| 11-11 02:31 | +5 | NEAR | UP | 0.60 | 0.65 | 0.17 |
| 11-11 02:31 | +10 stop | BNB | DOWN | 0.65 | 0.49 | -1.94 |
| 11-11 02:31 | +20 | BNB | DOWN | 0.65 | open |  |
| 11-11 02:31 | +15 | BNB | DOWN | 0.65 | open |  |
| 11-11 02:31 | +10 | BNB | DOWN | 0.64 | open |  |
| 11-11 02:31 | +5 | BNB | DOWN | 0.64 | open |  |
| 11-11 02:31 | +10 stop | ZEC | DOWN | 0.68 | open |  |
| 11-11 02:31 | +20 | ZEC | DOWN | 0.68 | open |  |
| 11-11 02:31 | +15 | ZEC | DOWN | 0.68 | open |  |
| 11-11 02:31 | +10 | ZEC | DOWN | 0.68 | open |  |
| 11-11 02:31 | +5 | ZEC | DOWN | 0.68 | 0.73 | 0.20 |
| 11-11 02:31 | +10 stop | BTC | DOWN | 0.61 | 0.42 | -2.25 |
| 11-11 02:31 | +20 | BTC | DOWN | 0.62 | open |  |
| 11-11 02:31 | +15 | BTC | DOWN | 0.62 | open |  |
| 11-11 02:31 | +10 | BTC | DOWN | 0.62 | open |  |
| 11-11 02:31 | +5 | BTC | DOWN | 0.61 | open |  |
| 11-11 02:30 | +10 stop | NEAR | DOWN | 0.50 | 0.64 | 1.05 |
| 11-11 02:30 | +20 | NEAR | DOWN | 0.50 | open |  |
| 11-11 02:30 | +15 | NEAR | DOWN | 0.50 | open |  |
| 11-11 02:30 | +10 | NEAR | DOWN | 0.50 | 0.64 | 1.05 |
| 11-11 02:30 | +5 | NEAR | DOWN | 0.50 | 0.64 | 1.05 |
| 11-11 02:29 | +10 stop | DOGE | UP | 0.06 | 0.67 | 5.90 |
| 11-11 02:29 | +20 | DOGE | UP | 0.07 | 0.67 | 5.84 |
| 11-11 02:29 | +15 | DOGE | UP | 0.07 | 0.67 | 5.79 |
| 11-11 02:29 | +10 | DOGE | UP | 0.07 | 0.67 | 5.75 |
| 11-11 02:29 | +5 | DOGE | UP | 0.07 | 0.67 | 5.75 |
| 11-11 02:26 | +20 | DOGE | UP | 0.70 | 0.90 | 1.78 |
| 11-11 02:26 | +15 | DOGE | UP | 0.70 | 0.85 | 1.26 |
| 11-11 02:26 | +10 | DOGE | UP | 0.70 | 0.82 | 0.94 |
| 11-11 02:26 | +5 | DOGE | UP | 0.70 | 0.82 | 0.94 |
| 11-11 02:26 | +10 stop | BTC | UP | 0.60 | 0.75 | 1.19 |
| 11-11 02:26 | +20 | BTC | UP | 0.62 | 0.88 | 2.35 |
