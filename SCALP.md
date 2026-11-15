# Range-Scalp Bot

*Updated Sun Nov 15 12:10 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 60718 | 52972 | 7746 (112) | 4 | $-16434.71 | -4.3% |
| **+10¢** | 45362 | 36280 | 9082 (150) | 6 | $-15511.30 | -5.4% |
| **+15¢** | 37996 | 28199 | 9797 (188) | 7 | $-14186.15 | -6.0% |
| **+20¢** | 33865 | 23589 | 10276 (240) | 7 | $-12472.61 | -5.9% |
| **+10¢ (15¢ stop)** | 73896 | 73745 | 151 (89) | 4 | $-27170.22 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-15 12:10 | +10 stop | DOGE | DOWN | 0.60 | open |  |
| 11-15 12:10 | +10 | DOGE | DOWN | 0.56 | open |  |
| 11-15 12:10 | +5 | DOGE | DOWN | 0.56 | 0.63 | 0.38 |
| 11-15 12:10 | +10 stop | ETH | DOWN | 0.70 | open |  |
| 11-15 12:10 | +20 | ETH | DOWN | 0.70 | open |  |
| 11-15 12:10 | +15 | ETH | DOWN | 0.70 | open |  |
| 11-15 12:10 | +10 | ETH | DOWN | 0.70 | open |  |
| 11-15 12:10 | +5 | ETH | DOWN | 0.70 | open |  |
| 11-15 12:10 | +5 | SOL | UP | 0.47 | 0.56 | 0.54 |
| 11-15 12:09 | +10 stop | BNB | UP | 0.57 | open |  |
| 11-15 12:09 | +10 stop | DOGE | DOWN | 0.51 | 0.65 | 1.06 |
| 11-15 12:09 | +20 | DOGE | DOWN | 0.51 | open |  |
| 11-15 12:09 | +15 | DOGE | DOWN | 0.51 | open |  |
| 11-15 12:09 | +10 | DOGE | DOWN | 0.51 | 0.65 | 1.06 |
| 11-15 12:09 | +5 | DOGE | DOWN | 0.52 | 0.65 | 0.96 |
| 11-15 12:09 | +10 stop | BTC | DOWN | 0.57 | 0.67 | 0.66 |
| 11-15 12:09 | +15 | BTC | DOWN | 0.57 | open |  |
| 11-15 12:09 | +10 | BTC | DOWN | 0.57 | 0.67 | 0.66 |
| 11-15 12:09 | +5 | BTC | DOWN | 0.57 | 0.67 | 0.66 |
| 11-15 12:09 | +10 stop | SOL | DOWN | 0.54 | open |  |
| 11-15 12:09 | +20 | SOL | DOWN | 0.54 | open |  |
| 11-15 12:09 | +15 | SOL | DOWN | 0.54 | open |  |
| 11-15 12:09 | +10 | SOL | DOWN | 0.54 | open |  |
| 11-15 12:09 | +5 | SOL | DOWN | 0.54 | 0.61 | 0.35 |
| 11-15 12:08 | +10 stop | XRP | UP | 0.70 | 0.80 | 0.73 |
| 11-15 12:08 | +10 | BNB | DOWN | 0.65 | open |  |
| 11-15 12:08 | +5 | BNB | DOWN | 0.62 | open |  |
| 11-15 12:08 | +10 stop | BNB | DOWN | 0.60 | 0.43 | -2.05 |
| 11-15 12:08 | +15 | BNB | DOWN | 0.60 | open |  |
| 11-15 12:08 | +10 | BNB | DOWN | 0.58 | 0.68 | 0.66 |
| 11-15 12:08 | +5 | BNB | DOWN | 0.60 | 0.68 | 0.47 |
| 11-15 12:07 | +10 stop | NEAR | UP | 0.58 | 0.70 | 0.87 |
| 11-15 12:07 | +10 stop | XRP | DOWN | 0.61 | 0.39 | -2.54 |
| 11-15 12:07 | +20 | XRP | DOWN | 0.61 | open |  |
| 11-15 12:07 | +15 | XRP | DOWN | 0.61 | open |  |
| 11-15 12:07 | +10 | XRP | DOWN | 0.61 | open |  |
| 11-15 12:07 | +5 | XRP | DOWN | 0.61 | open |  |
| 11-15 12:05 | +10 stop | NEAR | DOWN | 0.67 | 0.45 | -2.54 |
| 11-15 12:05 | +15 | NEAR | DOWN | 0.68 | open |  |
| 11-15 12:05 | +10 | NEAR | DOWN | 0.68 | open |  |
