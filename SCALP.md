# Range-Scalp Bot

*Updated Mon Nov 09 23:41 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 54034 | 47130 | 6904 (89) | 1 | $-14758.80 | -4.3% |
| **+10¢** | 40358 | 32304 | 8054 (117) | 2 | $-13716.35 | -5.4% |
| **+15¢** | 33825 | 25144 | 8681 (149) | 3 | $-12490.45 | -5.9% |
| **+20¢** | 30113 | 21008 | 9105 (195) | 4 | $-10931.44 | -5.8% |
| **+10¢ (15¢ stop)** | 65817 | 65707 | 110 (66) | 0 | $-24357.67 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-09 23:40 | +10 stop | XRP | UP | 0.57 | 0.42 | -1.86 |
| 11-09 23:40 | +5 | XRP | UP | 0.57 | 0.64 | 0.35 |
| 11-09 23:37 | +10 stop | XRP | DOWN | 0.62 | 0.32 | -3.33 |
| 11-09 23:36 | +5 | BNB | DOWN | 0.66 | 0.78 | 0.91 |
| 11-09 23:35 | +10 stop | DOGE | DOWN | 0.63 | 0.74 | 0.79 |
| 11-09 23:35 | +10 stop | NEAR | DOWN | 0.63 | 0.84 | 1.83 |
| 11-09 23:34 | +10 stop | XRP | DOWN | 0.69 | 0.80 | 0.83 |
| 11-09 23:34 | +5 | BNB | DOWN | 0.66 | 0.71 | 0.19 |
| 11-09 23:33 | +10 stop | DOGE | DOWN | 0.71 | 0.48 | -2.63 |
| 11-09 23:33 | +20 | DOGE | DOWN | 0.71 | open |  |
| 11-09 23:33 | +15 | DOGE | DOWN | 0.71 | 0.87 | 1.37 |
| 11-09 23:33 | +10 | DOGE | DOWN | 0.71 | 0.81 | 0.74 |
| 11-09 23:33 | +5 | DOGE | DOWN | 0.71 | 0.76 | 0.22 |
| 11-09 23:32 | +10 stop | XRP | DOWN | 0.66 | 0.76 | 0.71 |
| 11-09 23:32 | +10 stop | NEAR | DOWN | 0.62 | 0.46 | -1.95 |
| 11-09 23:32 | +10 stop | BNB | DOWN | 0.69 | 0.80 | 0.87 |
| 11-09 23:32 | +20 | BNB | DOWN | 0.69 | open |  |
| 11-09 23:32 | +15 | BNB | DOWN | 0.69 | open |  |
| 11-09 23:32 | +10 | BNB | DOWN | 0.69 | 0.80 | 0.87 |
| 11-09 23:32 | +5 | BNB | DOWN | 0.69 | 0.74 | 0.25 |
| 11-09 23:31 | +10 stop | ZEC | DOWN | 0.68 | 0.87 | 1.66 |
| 11-09 23:31 | +20 | ZEC | DOWN | 0.68 | 0.90 | 2.00 |
| 11-09 23:31 | +15 | ZEC | DOWN | 0.68 | 0.87 | 1.66 |
| 11-09 23:31 | +10 | ZEC | DOWN | 0.68 | 0.87 | 1.66 |
| 11-09 23:31 | +5 | ZEC | DOWN | 0.68 | 0.73 | 0.20 |
| 11-09 23:31 | +10 stop | HYPE | DOWN | 0.69 | 0.79 | 0.73 |
| 11-09 23:31 | +20 | HYPE | DOWN | 0.69 | 0.90 | 1.89 |
| 11-09 23:31 | +15 | HYPE | DOWN | 0.69 | 0.84 | 1.25 |
| 11-09 23:31 | +10 | HYPE | DOWN | 0.69 | 0.79 | 0.73 |
| 11-09 23:31 | +5 | HYPE | DOWN | 0.69 | 0.75 | 0.31 |
| 11-09 23:31 | +10 stop | BTC | DOWN | 0.64 | 0.74 | 0.69 |
| 11-09 23:31 | +20 | BTC | DOWN | 0.64 | 0.87 | 2.05 |
| 11-09 23:31 | +15 | BTC | DOWN | 0.64 | 0.79 | 1.21 |
| 11-09 23:31 | +10 | BTC | DOWN | 0.65 | 0.79 | 1.12 |
| 11-09 23:31 | +5 | BTC | DOWN | 0.65 | 0.73 | 0.50 |
| 11-09 23:31 | +10 stop | ETH | DOWN | 0.71 | 0.83 | 0.95 |
| 11-09 23:31 | +20 | ETH | DOWN | 0.71 | 0.91 | 1.80 |
| 11-09 23:31 | +15 | ETH | DOWN | 0.71 | 0.87 | 1.37 |
| 11-09 23:31 | +10 stop | XRP | UP | 0.62 | 0.33 | -3.28 |
| 11-09 23:31 | +20 | XRP | UP | 0.62 | open |  |
