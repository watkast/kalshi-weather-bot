# Range-Scalp Bot

*Updated Wed Nov 18 17:35 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 64271 | 56053 | 8218 (124) | 4 | $-17564.86 | -4.3% |
| **+10¢** | 48003 | 38387 | 9616 (165) | 7 | $-16448.41 | -5.5% |
| **+15¢** | 40242 | 29877 | 10365 (210) | 8 | $-14897.65 | -5.9% |
| **+20¢** | 35833 | 24954 | 10879 (265) | 8 | $-13196.17 | -5.9% |
| **+10¢ (15¢ stop)** | 78189 | 78025 | 164 (98) | 4 | $-28789.89 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-18 17:34 | +10 stop | SOL | UP | 0.69 | open |  |
| 11-18 17:34 | +10 | SOL | UP | 0.70 | open |  |
| 11-18 17:34 | +5 | SOL | UP | 0.70 | open |  |
| 11-18 17:34 | +10 stop | DOGE | UP | 0.71 | open |  |
| 11-18 17:33 | +10 stop | XRP | UP | 0.60 | open |  |
| 11-18 17:33 | +10 stop | HYPE | UP | 0.62 | open |  |
| 11-18 17:32 | +10 stop | SOL | UP | 0.64 | 0.75 | 0.79 |
| 11-18 17:32 | +10 | SOL | UP | 0.64 | 0.75 | 0.79 |
| 11-18 17:32 | +5 | SOL | UP | 0.64 | 0.72 | 0.48 |
| 11-18 17:32 | +10 stop | DOGE | DOWN | 0.52 | 0.30 | -2.53 |
| 11-18 17:32 | +10 | DOGE | DOWN | 0.53 | open |  |
| 11-18 17:32 | +5 | DOGE | DOWN | 0.56 | open |  |
| 11-18 17:32 | +10 stop | HYPE | DOWN | 0.57 | 0.42 | -1.86 |
| 11-18 17:32 | +20 | HYPE | DOWN | 0.57 | open |  |
| 11-18 17:32 | +15 | HYPE | DOWN | 0.57 | open |  |
| 11-18 17:32 | +10 | HYPE | DOWN | 0.57 | open |  |
| 11-18 17:32 | +5 | HYPE | DOWN | 0.57 | open |  |
| 11-18 17:32 | +5 | BNB | UP | 0.50 | 0.55 | 0.14 |
| 11-18 17:32 | +10 stop | ETH | UP | 0.61 | 0.81 | 1.72 |
| 11-18 17:32 | +20 | ETH | UP | 0.62 | 0.86 | 2.14 |
| 11-18 17:32 | +15 | ETH | UP | 0.62 | 0.81 | 1.62 |
| 11-18 17:32 | +10 | ETH | UP | 0.62 | 0.81 | 1.62 |
| 11-18 17:32 | +5 | ETH | UP | 0.62 | 0.81 | 1.62 |
| 11-18 17:32 | +10 stop | ZEC | UP | 0.56 | 0.71 | 1.17 |
| 11-18 17:32 | +5 | ZEC | UP | 0.57 | 0.71 | 1.07 |
| 11-18 17:32 | +5 | NEAR | UP | 0.58 | 0.63 | 0.15 |
| 11-18 17:31 | +10 stop | XRP | DOWN | 0.60 | 0.42 | -2.15 |
| 11-18 17:31 | +20 | XRP | DOWN | 0.60 | open |  |
| 11-18 17:31 | +15 | XRP | DOWN | 0.60 | open |  |
| 11-18 17:31 | +10 | XRP | DOWN | 0.58 | open |  |
| 11-18 17:31 | +5 | XRP | DOWN | 0.59 | open |  |
| 11-18 17:31 | +10 stop | DOGE | DOWN | 0.46 | 0.58 | 0.84 |
| 11-18 17:31 | +20 | DOGE | DOWN | 0.46 | open |  |
| 11-18 17:31 | +15 | DOGE | DOWN | 0.46 | open |  |
| 11-18 17:31 | +10 | DOGE | DOWN | 0.46 | 0.58 | 0.84 |
| 11-18 17:31 | +5 | DOGE | DOWN | 0.46 | 0.55 | 0.54 |
| 11-18 17:31 | +10 stop | BTC | DOWN | 0.50 | 0.63 | 0.95 |
| 11-18 17:31 | +20 | BTC | DOWN | 0.49 | open |  |
| 11-18 17:31 | +15 | BTC | DOWN | 0.49 | open |  |
| 11-18 17:31 | +10 | BTC | DOWN | 0.49 | 0.63 | 1.05 |
