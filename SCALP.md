# Range-Scalp Bot

*Updated Mon Nov 09 21:29 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 53904 | 47013 | 6891 (89) | 2 | $-14753.16 | -4.3% |
| **+10¢** | 40263 | 32221 | 8042 (117) | 1 | $-13743.23 | -5.4% |
| **+15¢** | 33743 | 25075 | 8668 (149) | 1 | $-12521.53 | -5.9% |
| **+20¢** | 30038 | 20946 | 9092 (195) | 1 | $-10981.39 | -5.8% |
| **+10¢ (15¢ stop)** | 65676 | 65566 | 110 (66) | 0 | $-24327.23 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-09 21:28 | +10 stop | BTC | UP | 0.69 | 0.87 | 1.57 |
| 11-09 21:28 | +10 stop | BNB | DOWN | 0.30 | 0.65 | 3.19 |
| 11-09 21:27 | +10 stop | DOGE | DOWN | 0.65 | 0.13 | -5.44 |
| 11-09 21:27 | +5 | DOGE | DOWN | 0.65 | open |  |
| 11-09 21:26 | +10 stop | BNB | UP | 0.62 | 0.44 | -2.15 |
| 11-09 21:25 | +5 | BTC | UP | 0.64 | 0.74 | 0.69 |
| 11-09 21:25 | +10 stop | BNB | DOWN | 0.60 | 0.38 | -2.54 |
| 11-09 21:25 | +10 stop | BTC | UP | 0.58 | 0.33 | -2.84 |
| 11-09 21:25 | +5 | BTC | UP | 0.58 | 0.63 | 0.15 |
| 11-09 21:25 | +10 stop | SOL | DOWN | 0.71 | 0.93 | 1.98 |
| 11-09 21:24 | +10 stop | DOGE | UP | 0.63 | 0.40 | -2.64 |
| 11-09 21:24 | +15 | DOGE | UP | 0.63 | 0.86 | 2.04 |
| 11-09 21:24 | +10 | DOGE | UP | 0.63 | 0.86 | 2.04 |
| 11-09 21:24 | +5 | DOGE | UP | 0.63 | 0.71 | 0.48 |
| 11-09 21:23 | +10 stop | BNB | UP | 0.53 | 0.36 | -2.05 |
| 11-09 21:23 | +10 stop | SOL | UP | 0.65 | 0.27 | -4.10 |
| 11-09 21:21 | +10 stop | BNB | DOWN | 0.60 | 0.38 | -2.54 |
| 11-09 21:21 | +10 stop | DOGE | UP | 0.56 | 0.70 | 1.07 |
| 11-09 21:21 | +10 stop | DOGE | DOWN | 0.47 | 0.67 | 1.66 |
| 11-09 21:21 | +10 stop | ZEC | DOWN | 0.50 | 0.61 | 0.75 |
| 11-09 21:21 | +5 | ZEC | DOWN | 0.49 | 0.61 | 0.85 |
| 11-09 21:20 | +10 stop | SOL | DOWN | 0.68 | 0.49 | -2.24 |
| 11-09 21:20 | +10 stop | BTC | DOWN | 0.58 | 0.35 | -2.64 |
| 11-09 21:20 | +5 | ETH | UP | 0.67 | 0.75 | 0.50 |
| 11-09 21:20 | +20 | ZEC | UP | 0.53 | 0.78 | 2.19 |
| 11-09 21:20 | +5 | ZEC | UP | 0.53 | 0.60 | 0.35 |
| 11-09 21:20 | +10 stop | XRP | UP | 0.67 | 0.81 | 1.10 |
| 11-09 21:20 | +20 | XRP | UP | 0.67 | 0.87 | 1.76 |
| 11-09 21:20 | +15 | XRP | UP | 0.67 | 0.86 | 1.65 |
| 11-09 21:20 | +10 | XRP | UP | 0.67 | 0.81 | 1.10 |
| 11-09 21:20 | +5 | XRP | UP | 0.67 | 0.76 | 0.58 |
| 11-09 21:18 | +15 | ZEC | UP | 0.64 | 0.82 | 1.53 |
| 11-09 21:17 | +10 stop | ZEC | UP | 0.69 | 0.50 | -2.23 |
| 11-09 21:17 | +10 | ZEC | UP | 0.68 | 0.78 | 0.71 |
| 11-09 21:17 | +5 | ZEC | UP | 0.68 | 0.74 | 0.30 |
| 11-09 21:17 | +10 stop | BTC | UP | 0.67 | 0.52 | -1.84 |
| 11-09 21:17 | +20 | BTC | UP | 0.67 | 0.87 | 1.76 |
| 11-09 21:17 | +15 | BTC | UP | 0.67 | 0.87 | 1.76 |
| 11-09 21:17 | +10 | BTC | UP | 0.67 | 0.87 | 1.76 |
| 11-09 21:17 | +5 | BTC | UP | 0.67 | 0.73 | 0.30 |
