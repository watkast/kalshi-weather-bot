# Range-Scalp Bot

*Updated Fri Nov 20 02:46 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 65731 | 57375 | 8356 (124) | 1 | $-17622.97 | -4.3% |
| **+10¢** | 49094 | 39322 | 9772 (165) | 1 | $-16400.16 | -5.3% |
| **+15¢** | 41176 | 30634 | 10542 (211) | 1 | $-14774.67 | -5.7% |
| **+20¢** | 36654 | 25580 | 11074 (267) | 1 | $-13086.58 | -5.7% |
| **+10¢ (15¢ stop)** | 80011 | 79847 | 164 (98) | 1 | $-29453.89 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-20 02:46 | +10 stop | DOGE | DOWN | 0.56 | open |  |
| 11-20 02:46 | +20 | DOGE | DOWN | 0.58 | open |  |
| 11-20 02:46 | +15 | DOGE | DOWN | 0.58 | open |  |
| 11-20 02:46 | +10 | DOGE | DOWN | 0.58 | open |  |
| 11-20 02:46 | +5 | DOGE | DOWN | 0.58 | open |  |
| 11-20 02:37 | +10 stop | XRP | UP | 0.71 | 0.81 | 0.74 |
| 11-20 02:37 | +5 | XRP | UP | 0.71 | 0.79 | 0.53 |
| 11-20 02:37 | +10 stop | BNB | UP | 0.69 | 0.83 | 1.15 |
| 11-20 02:37 | +5 | BNB | UP | 0.69 | 0.83 | 1.15 |
| 11-20 02:36 | +10 stop | HYPE | UP | 0.67 | 0.78 | 0.81 |
| 11-20 02:35 | +10 stop | BTC | DOWN | 0.53 | 0.36 | -2.05 |
| 11-20 02:35 | +10 stop | ETH | DOWN | 0.59 | 0.31 | -3.12 |
| 11-20 02:35 | +10 stop | XRP | DOWN | 0.65 | 0.41 | -2.73 |
| 11-20 02:35 | +5 | ZEC | UP | 0.48 | 0.56 | 0.44 |
| 11-20 02:35 | +10 stop | NEAR | UP | 0.59 | 0.76 | 1.40 |
| 11-20 02:34 | +10 stop | SOL | DOWN | 0.51 | 0.33 | -2.14 |
| 11-20 02:34 | +10 stop | ZEC | UP | 0.55 | 0.72 | 1.37 |
| 11-20 02:33 | +10 stop | XRP | DOWN | 0.65 | 0.49 | -1.94 |
| 11-20 02:33 | +10 stop | DOGE | DOWN | 0.57 | 0.38 | -2.25 |
| 11-20 02:33 | +10 stop | HYPE | DOWN | 0.62 | 0.45 | -2.05 |
| 11-20 02:33 | +10 stop | BNB | DOWN | 0.66 | 0.48 | -2.14 |
| 11-20 02:32 | +5 | BTC | UP | 0.58 | 0.63 | 0.15 |
| 11-20 02:32 | +5 | ZEC | UP | 0.56 | 0.63 | 0.35 |
| 11-20 02:32 | +5 | XRP | UP | 0.53 | 0.58 | 0.14 |
| 11-20 02:31 | +10 stop | BNB | UP | 0.63 | 0.48 | -1.85 |
| 11-20 02:31 | +20 | BNB | UP | 0.63 | 0.83 | 1.73 |
| 11-20 02:31 | +15 | BNB | UP | 0.63 | 0.83 | 1.73 |
| 11-20 02:31 | +10 | BNB | UP | 0.64 | 0.83 | 1.63 |
| 11-20 02:31 | +5 | BNB | UP | 0.64 | 0.70 | 0.28 |
| 11-20 02:31 | +10 stop | DOGE | UP | 0.64 | 0.48 | -1.99 |
| 11-20 02:31 | +20 | DOGE | UP | 0.64 | 0.94 | 2.69 |
| 11-20 02:31 | +15 | DOGE | UP | 0.65 | 0.80 | 1.24 |
| 11-20 02:31 | +10 | DOGE | UP | 0.65 | 0.80 | 1.24 |
| 11-20 02:31 | +5 | DOGE | UP | 0.64 | 0.73 | 0.55 |
| 11-20 02:31 | +10 stop | HYPE | UP | 0.62 | 0.46 | -1.95 |
| 11-20 02:31 | +20 | HYPE | UP | 0.62 | 0.88 | 2.35 |
| 11-20 02:31 | +15 | HYPE | UP | 0.62 | 0.78 | 1.30 |
| 11-20 02:31 | +10 | HYPE | UP | 0.62 | 0.73 | 0.79 |
| 11-20 02:31 | +5 | HYPE | UP | 0.62 | 0.70 | 0.48 |
| 11-20 02:31 | +10 stop | SOL | UP | 0.66 | 0.49 | -2.04 |
