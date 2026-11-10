# Range-Scalp Bot

*Updated Tue Nov 10 00:33 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 54086 | 47178 | 6908 (89) | 0 | $-14747.67 | -4.3% |
| **+10¢** | 40399 | 32339 | 8060 (117) | 2 | $-13707.96 | -5.4% |
| **+15¢** | 33861 | 25174 | 8687 (149) | 2 | $-12471.73 | -5.9% |
| **+20¢** | 30148 | 21037 | 9111 (195) | 2 | $-10900.22 | -5.8% |
| **+10¢ (15¢ stop)** | 65883 | 65773 | 110 (66) | 1 | $-24367.20 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-10 00:31 | +10 stop | ZEC | DOWN | 0.68 | 0.78 | 0.71 |
| 11-10 00:31 | +20 | ZEC | DOWN | 0.69 | open |  |
| 11-10 00:31 | +15 | ZEC | DOWN | 0.69 | open |  |
| 11-10 00:31 | +10 | ZEC | DOWN | 0.70 | open |  |
| 11-10 00:31 | +5 | ZEC | DOWN | 0.71 | 0.78 | 0.42 |
| 11-10 00:31 | +10 stop | BNB | DOWN | 0.65 | open |  |
| 11-10 00:31 | +20 | BNB | DOWN | 0.65 | open |  |
| 11-10 00:31 | +15 | BNB | DOWN | 0.65 | open |  |
| 11-10 00:31 | +10 | BNB | DOWN | 0.65 | open |  |
| 11-10 00:31 | +5 | BNB | DOWN | 0.65 | 0.72 | 0.39 |
| 11-10 00:26 | +10 stop | XRP | UP | 0.64 | 0.80 | 1.31 |
| 11-10 00:26 | +5 | XRP | UP | 0.65 | 0.80 | 1.22 |
| 11-10 00:18 | +10 stop | XRP | DOWN | 0.65 | 0.76 | 0.81 |
| 11-10 00:18 | +5 | XRP | DOWN | 0.61 | 0.69 | 0.48 |
| 11-10 00:18 | +5 | DOGE | DOWN | 0.68 | 0.79 | 0.82 |
| 11-10 00:18 | +10 stop | ZEC | UP | 0.48 | 0.33 | -1.84 |
| 11-10 00:17 | +10 stop | DOGE | DOWN | 0.55 | 0.66 | 0.76 |
| 11-10 00:17 | +20 | DOGE | DOWN | 0.55 | 0.79 | 2.10 |
| 11-10 00:17 | +15 | DOGE | DOWN | 0.55 | 0.72 | 1.37 |
| 11-10 00:17 | +10 | DOGE | DOWN | 0.55 | 0.66 | 0.76 |
| 11-10 00:17 | +5 | DOGE | DOWN | 0.50 | 0.57 | 0.34 |
| 11-10 00:17 | +10 stop | NEAR | UP | 0.53 | 0.31 | -2.53 |
| 11-10 00:17 | +20 | NEAR | UP | 0.53 | no | -5.48 |
| 11-10 00:17 | +15 | NEAR | UP | 0.53 | no | -5.48 |
| 11-10 00:17 | +10 | NEAR | UP | 0.53 | no | -5.48 |
| 11-10 00:17 | +5 | NEAR | UP | 0.53 | no | -5.48 |
| 11-10 00:16 | +10 stop | BNB | DOWN | 0.65 | 0.75 | 0.70 |
| 11-10 00:16 | +20 | BNB | DOWN | 0.65 | 0.90 | 2.31 |
| 11-10 00:16 | +15 | BNB | DOWN | 0.65 | 0.80 | 1.22 |
| 11-10 00:16 | +10 | BNB | DOWN | 0.65 | 0.75 | 0.70 |
| 11-10 00:16 | +5 | BNB | DOWN | 0.65 | 0.74 | 0.60 |
| 11-10 00:16 | +10 stop | ZEC | UP | 0.71 | 0.53 | -2.13 |
| 11-10 00:16 | +10 | ZEC | UP | 0.71 | 0.83 | 0.95 |
| 11-10 00:16 | +5 | ZEC | UP | 0.70 | 0.78 | 0.47 |
| 11-10 00:16 | +10 stop | XRP | UP | 0.61 | 0.45 | -1.95 |
| 11-10 00:16 | +20 | XRP | UP | 0.61 | 0.87 | 2.35 |
| 11-10 00:16 | +15 | XRP | UP | 0.60 | 0.80 | 1.71 |
| 11-10 00:16 | +10 | XRP | UP | 0.60 | 0.80 | 1.71 |
| 11-10 00:16 | +5 | XRP | UP | 0.62 | 0.67 | 0.17 |
| 11-10 00:15 | +10 stop | BTC | DOWN | 0.69 | 0.82 | 1.04 |
