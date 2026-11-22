# Range-Scalp Bot

*Updated Sun Nov 22 20:59 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 69086 | 60285 | 8801 (145) | 5 | $-18573.08 | -4.3% |
| **+10¢** | 51556 | 41280 | 10276 (188) | 5 | $-17212.95 | -5.3% |
| **+15¢** | 43207 | 32132 | 11075 (240) | 5 | $-15425.76 | -5.7% |
| **+20¢** | 38476 | 26838 | 11638 (299) | 5 | $-13707.93 | -5.7% |
| **+10¢ (15¢ stop)** | 84135 | 83946 | 189 (117) | 0 | $-30967.83 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-22 20:51 | +10 stop | SOL | UP | 0.66 | 0.76 | 0.71 |
| 11-22 20:51 | +10 stop | SOL | UP | 0.58 | 0.68 | 0.66 |
| 11-22 20:50 | +10 stop | NEAR | UP | 0.62 | 0.74 | 0.87 |
| 11-22 20:50 | +10 stop | SOL | UP | 0.64 | 0.41 | -2.64 |
| 11-22 20:49 | +5 | XRP | UP | 0.71 | 0.77 | 0.32 |
| 11-22 20:48 | +10 stop | ETH | UP | 0.58 | 0.71 | 0.97 |
| 11-22 20:48 | +20 | ETH | UP | 0.58 | 0.82 | 2.11 |
| 11-22 20:48 | +15 | ETH | UP | 0.58 | 0.75 | 1.38 |
| 11-22 20:48 | +10 | ETH | UP | 0.58 | 0.71 | 0.97 |
| 11-22 20:48 | +5 | ETH | UP | 0.58 | 0.63 | 0.15 |
| 11-22 20:47 | +10 stop | ZEC | UP | 0.58 | 0.69 | 0.77 |
| 11-22 20:47 | +10 stop | BNB | UP | 0.67 | 0.80 | 1.02 |
| 11-22 20:47 | +20 | BNB | UP | 0.67 | 0.95 | 2.65 |
| 11-22 20:47 | +15 | BNB | UP | 0.67 | 0.82 | 1.23 |
| 11-22 20:47 | +10 | BNB | UP | 0.67 | 0.80 | 1.02 |
| 11-22 20:47 | +5 | BNB | UP | 0.67 | 0.80 | 1.02 |
| 11-22 20:47 | +10 stop | SOL | DOWN | 0.59 | 0.38 | -2.44 |
| 11-22 20:47 | +20 | SOL | DOWN | 0.58 | open |  |
| 11-22 20:47 | +15 | SOL | DOWN | 0.58 | open |  |
| 11-22 20:47 | +10 | SOL | DOWN | 0.58 | open |  |
| 11-22 20:47 | +5 | SOL | DOWN | 0.58 | open |  |
| 11-22 20:47 | +10 stop | DOGE | DOWN | 0.57 | 0.41 | -1.95 |
| 11-22 20:47 | +20 | DOGE | DOWN | 0.57 | open |  |
| 11-22 20:47 | +15 | DOGE | DOWN | 0.57 | open |  |
| 11-22 20:47 | +10 | DOGE | DOWN | 0.57 | open |  |
| 11-22 20:47 | +5 | DOGE | DOWN | 0.58 | open |  |
| 11-22 20:47 | +10 stop | HYPE | DOWN | 0.59 | 0.36 | -2.62 |
| 11-22 20:47 | +20 | HYPE | DOWN | 0.59 | open |  |
| 11-22 20:47 | +15 | HYPE | DOWN | 0.59 | open |  |
| 11-22 20:47 | +10 | HYPE | DOWN | 0.59 | open |  |
| 11-22 20:47 | +5 | HYPE | DOWN | 0.59 | open |  |
| 11-22 20:46 | +10 stop | ZEC | UP | 0.69 | 0.53 | -1.93 |
| 11-22 20:46 | +20 | ZEC | UP | 0.69 | 0.89 | 1.78 |
| 11-22 20:45 | +10 stop | NEAR | DOWN | 0.64 | 0.42 | -2.55 |
| 11-22 20:45 | +20 | NEAR | DOWN | 0.64 | open |  |
| 11-22 20:45 | +15 | NEAR | DOWN | 0.64 | open |  |
| 11-22 20:45 | +10 | NEAR | DOWN | 0.64 | open |  |
| 11-22 20:45 | +5 | NEAR | DOWN | 0.64 | open |  |
| 11-22 20:45 | +10 stop | BTC | DOWN | 0.61 | 0.45 | -1.95 |
| 11-22 20:45 | +20 | BTC | DOWN | 0.61 | open |  |
