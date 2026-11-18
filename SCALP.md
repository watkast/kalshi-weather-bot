# Range-Scalp Bot

*Updated Wed Nov 18 18:15 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 64320 | 56098 | 8222 (124) | 3 | $-17565.32 | -4.3% |
| **+10¢** | 48041 | 38423 | 9618 (165) | 2 | $-16417.07 | -5.4% |
| **+15¢** | 40276 | 29911 | 10365 (210) | 2 | $-14843.00 | -5.9% |
| **+20¢** | 35864 | 24985 | 10879 (265) | 2 | $-13133.24 | -5.8% |
| **+10¢ (15¢ stop)** | 78252 | 78088 | 164 (98) | 0 | $-28824.18 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-18 18:13 | +10 stop | SOL | DOWN | 0.69 | 0.47 | -2.53 |
| 11-18 18:13 | +5 | SOL | DOWN | 0.69 | open |  |
| 11-18 18:13 | +10 stop | BTC | UP | 0.57 | 0.93 | 3.35 |
| 11-18 18:12 | +10 stop | XRP | DOWN | 0.58 | 0.41 | -2.09 |
| 11-18 18:12 | +10 stop | DOGE | DOWN | 0.57 | 0.41 | -1.95 |
| 11-18 18:12 | +10 | DOGE | DOWN | 0.57 | open |  |
| 11-18 18:12 | +5 | DOGE | DOWN | 0.57 | open |  |
| 11-18 18:12 | +10 stop | BTC | DOWN | 0.60 | 0.45 | -1.85 |
| 11-18 18:11 | +10 stop | BTC | UP | 0.69 | 0.47 | -2.53 |
| 11-18 18:11 | +10 stop | SOL | DOWN | 0.66 | 0.80 | 1.12 |
| 11-18 18:11 | +5 | SOL | DOWN | 0.66 | 0.80 | 1.12 |
| 11-18 18:10 | +10 stop | DOGE | UP | 0.61 | 0.26 | -3.81 |
| 11-18 18:10 | +10 stop | HYPE | UP | 0.64 | 0.75 | 0.79 |
| 11-18 18:10 | +10 | HYPE | UP | 0.64 | 0.75 | 0.79 |
| 11-18 18:10 | +5 | HYPE | UP | 0.64 | 0.71 | 0.38 |
| 11-18 18:10 | +10 stop | BNB | DOWN | 0.69 | 0.87 | 1.57 |
| 11-18 18:10 | +15 | BNB | DOWN | 0.69 | 0.87 | 1.57 |
| 11-18 18:10 | +10 | BNB | DOWN | 0.69 | 0.87 | 1.57 |
| 11-18 18:10 | +5 | BNB | DOWN | 0.69 | 0.87 | 1.57 |
| 11-18 18:09 | +10 stop | ETH | DOWN | 0.59 | 0.71 | 0.88 |
| 11-18 18:09 | +20 | ETH | DOWN | 0.59 | 0.85 | 2.34 |
| 11-18 18:09 | +15 | ETH | DOWN | 0.59 | 0.74 | 1.19 |
| 11-18 18:09 | +10 | ETH | DOWN | 0.59 | 0.71 | 0.88 |
| 11-18 18:09 | +5 | ETH | DOWN | 0.58 | 0.64 | 0.25 |
| 11-18 18:09 | +10 stop | BNB | DOWN | 0.51 | 0.67 | 1.26 |
| 11-18 18:09 | +20 | BNB | DOWN | 0.51 | 0.73 | 1.88 |
| 11-18 18:09 | +15 | BNB | DOWN | 0.52 | 0.67 | 1.16 |
| 11-18 18:09 | +10 | BNB | DOWN | 0.52 | 0.67 | 1.16 |
| 11-18 18:09 | +5 | BNB | DOWN | 0.52 | 0.67 | 1.16 |
| 11-18 18:09 | +10 stop | XRP | DOWN | 0.66 | 0.50 | -1.94 |
| 11-18 18:09 | +10 stop | DOGE | DOWN | 0.65 | 0.39 | -2.93 |
| 11-18 18:09 | +15 | DOGE | DOWN | 0.65 | open |  |
| 11-18 18:09 | +10 | DOGE | DOWN | 0.65 | 0.76 | 0.81 |
| 11-18 18:09 | +5 | DOGE | DOWN | 0.65 | 0.73 | 0.50 |
| 11-18 18:08 | +10 stop | HYPE | DOWN | 0.61 | 0.30 | -3.42 |
| 11-18 18:07 | +10 stop | BTC | UP | 0.68 | 0.45 | -2.64 |
| 11-18 18:07 | +10 stop | BNB | DOWN | 0.54 | 0.79 | 2.20 |
| 11-18 18:07 | +20 | BNB | DOWN | 0.54 | 0.79 | 2.20 |
| 11-18 18:07 | +15 | BNB | DOWN | 0.53 | 0.79 | 2.30 |
| 11-18 18:07 | +10 | BNB | DOWN | 0.53 | 0.79 | 2.28 |
