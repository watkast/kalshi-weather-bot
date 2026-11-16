# Range-Scalp Bot

*Updated Mon Nov 16 10:54 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 61927 | 54027 | 7900 (115) | 1 | $-16756.64 | -4.3% |
| **+10¢** | 46259 | 37013 | 9246 (157) | 2 | $-15631.46 | -5.4% |
| **+15¢** | 38764 | 28795 | 9969 (196) | 2 | $-14210.62 | -5.8% |
| **+20¢** | 34558 | 24105 | 10453 (249) | 3 | $-12398.19 | -5.7% |
| **+10¢ (15¢ stop)** | 75380 | 75226 | 154 (90) | 2 | $-27809.05 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-16 10:54 | +10 stop | SOL | UP | 0.68 | open |  |
| 11-16 10:54 | +10 stop | ETH | UP | 0.66 | open |  |
| 11-16 10:54 | +5 | ETH | UP | 0.66 | 0.71 | 0.19 |
| 11-16 10:54 | +10 stop | ZEC | DOWN | 0.39 | 0.61 | 1.86 |
| 11-16 10:54 | +20 | ZEC | DOWN | 0.39 | 0.61 | 1.86 |
| 11-16 10:54 | +15 | ZEC | DOWN | 0.39 | 0.61 | 1.86 |
| 11-16 10:54 | +10 | ZEC | DOWN | 0.38 | 0.61 | 1.96 |
| 11-16 10:54 | +5 | ZEC | DOWN | 0.38 | 0.61 | 1.96 |
| 11-16 10:53 | +10 stop | ETH | DOWN | 0.48 | 0.58 | 0.64 |
| 11-16 10:53 | +5 | ETH | DOWN | 0.48 | 0.58 | 0.64 |
| 11-16 10:53 | +10 stop | SOL | DOWN | 0.59 | 0.43 | -1.95 |
| 11-16 10:52 | +10 | BNB | UP | 0.56 | 0.74 | 1.48 |
| 11-16 10:52 | +5 | BNB | UP | 0.56 | 0.64 | 0.45 |
| 11-16 10:52 | +10 stop | NEAR | DOWN | 0.70 | 0.45 | -2.83 |
| 11-16 10:52 | +10 stop | ETH | DOWN | 0.60 | 0.70 | 0.68 |
| 11-16 10:52 | +10 stop | DOGE | DOWN | 0.57 | 0.35 | -2.54 |
| 11-16 10:52 | +15 | DOGE | DOWN | 0.58 | open |  |
| 11-16 10:52 | +10 | DOGE | DOWN | 0.58 | open |  |
| 11-16 10:52 | +5 | DOGE | DOWN | 0.58 | open |  |
| 11-16 10:52 | +10 stop | HYPE | DOWN | 0.70 | 0.46 | -2.73 |
| 11-16 10:52 | +10 stop | SOL | DOWN | 0.71 | 0.54 | -2.03 |
| 11-16 10:52 | +10 stop | XRP | UP | 0.44 | 0.55 | 0.74 |
| 11-16 10:52 | +15 | XRP | UP | 0.44 | 0.59 | 1.15 |
| 11-16 10:52 | +5 | XRP | UP | 0.45 | 0.55 | 0.64 |
| 11-16 10:52 | +10 stop | BNB | UP | 0.55 | 0.74 | 1.58 |
| 11-16 10:52 | +15 | BNB | UP | 0.54 | 0.74 | 1.69 |
| 11-16 10:52 | +10 | BNB | UP | 0.52 | 0.64 | 0.85 |
| 11-16 10:52 | +5 | BNB | UP | 0.52 | 0.64 | 0.85 |
| 11-16 10:50 | +5 | SOL | UP | 0.51 | 0.56 | 0.14 |
| 11-16 10:50 | +10 stop | ETH | UP | 0.61 | 0.39 | -2.54 |
| 11-16 10:49 | +10 | XRP | UP | 0.70 | 0.89 | 1.69 |
| 11-16 10:49 | +5 | XRP | UP | 0.70 | 0.76 | 0.33 |
| 11-16 10:49 | +10 stop | ETH | UP | 0.56 | 0.68 | 0.86 |
| 11-16 10:49 | +5 | ZEC | DOWN | 0.62 | 0.70 | 0.43 |
| 11-16 10:49 | +10 stop | DOGE | UP | 0.63 | 0.73 | 0.69 |
| 11-16 10:49 | +10 | DOGE | UP | 0.63 | 0.73 | 0.69 |
| 11-16 10:49 | +5 | DOGE | UP | 0.63 | 0.70 | 0.38 |
| 11-16 10:48 | +5 | XRP | UP | 0.59 | 0.69 | 0.68 |
| 11-16 10:48 | +10 stop | XRP | UP | 0.63 | 0.76 | 1.00 |
| 11-16 10:48 | +5 | BTC | DOWN | 0.62 | 0.75 | 0.99 |
