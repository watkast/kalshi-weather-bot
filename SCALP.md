# Range-Scalp Bot

*Updated Sun Nov 15 15:03 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 60943 | 53171 | 7772 (112) | 2 | $-16480.75 | -4.3% |
| **+10¢** | 45523 | 36417 | 9106 (150) | 4 | $-15496.38 | -5.4% |
| **+15¢** | 38119 | 28298 | 9821 (188) | 8 | $-14171.46 | -5.9% |
| **+20¢** | 33973 | 23672 | 10301 (240) | 9 | $-12449.77 | -5.8% |
| **+10¢ (15¢ stop)** | 74167 | 74016 | 151 (89) | 3 | $-27287.86 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-15 15:03 | +20 | ZEC | UP | 0.52 | open |  |
| 11-15 15:03 | +15 | ZEC | UP | 0.52 | open |  |
| 11-15 15:03 | +5 | HYPE | DOWN | 0.70 | open |  |
| 11-15 15:02 | +10 stop | ZEC | UP | 0.63 | 0.48 | -1.85 |
| 11-15 15:02 | +10 | ZEC | UP | 0.63 | open |  |
| 11-15 15:02 | +5 | ZEC | UP | 0.63 | open |  |
| 11-15 15:02 | +10 stop | XRP | DOWN | 0.66 | open |  |
| 11-15 15:02 | +20 | XRP | DOWN | 0.66 | open |  |
| 11-15 15:02 | +15 | XRP | DOWN | 0.67 | open |  |
| 11-15 15:02 | +10 | XRP | DOWN | 0.65 | open |  |
| 11-15 15:02 | +5 | XRP | DOWN | 0.65 | 0.73 | 0.50 |
| 11-15 15:02 | +5 | SOL | DOWN | 0.60 | 0.65 | 0.17 |
| 11-15 15:02 | +10 stop | DOGE | DOWN | 0.64 | 0.74 | 0.69 |
| 11-15 15:02 | +20 | DOGE | DOWN | 0.64 | open |  |
| 11-15 15:02 | +15 | DOGE | DOWN | 0.64 | open |  |
| 11-15 15:02 | +10 | DOGE | DOWN | 0.64 | 0.74 | 0.69 |
| 11-15 15:02 | +5 | DOGE | DOWN | 0.64 | 0.74 | 0.69 |
| 11-15 15:02 | +10 stop | NEAR | DOWN | 0.54 | open |  |
| 11-15 15:02 | +20 | NEAR | DOWN | 0.54 | open |  |
| 11-15 15:02 | +15 | NEAR | DOWN | 0.54 | open |  |
| 11-15 15:02 | +10 | NEAR | DOWN | 0.54 | open |  |
| 11-15 15:02 | +5 | NEAR | DOWN | 0.54 | 0.61 | 0.35 |
| 11-15 15:02 | +10 stop | ETH | DOWN | 0.63 | 0.76 | 1.00 |
| 11-15 15:02 | +20 | ETH | DOWN | 0.63 | open |  |
| 11-15 15:02 | +15 | ETH | DOWN | 0.64 | open |  |
| 11-15 15:02 | +10 | ETH | DOWN | 0.63 | 0.76 | 1.00 |
| 11-15 15:02 | +5 | ETH | DOWN | 0.63 | 0.76 | 1.00 |
| 11-15 15:02 | +5 | BNB | DOWN | 0.57 | 0.66 | 0.56 |
| 11-15 15:02 | +5 | HYPE | DOWN | 0.56 | 0.62 | 0.24 |
| 11-15 15:02 | +10 stop | BNB | DOWN | 0.58 | open |  |
| 11-15 15:02 | +10 stop | BTC | DOWN | 0.59 | 0.74 | 1.19 |
| 11-15 15:02 | +20 | BTC | DOWN | 0.59 | open |  |
| 11-15 15:02 | +15 | BTC | DOWN | 0.59 | 0.74 | 1.19 |
| 11-15 15:02 | +10 | BTC | DOWN | 0.59 | 0.74 | 1.19 |
| 11-15 15:02 | +5 | BTC | DOWN | 0.59 | 0.64 | 0.16 |
| 11-15 15:02 | +10 stop | HYPE | DOWN | 0.59 | 0.69 | 0.68 |
| 11-15 15:01 | +10 stop | ZEC | UP | 0.41 | 0.55 | 1.05 |
| 11-15 15:01 | +20 | ZEC | UP | 0.41 | 0.65 | 2.07 |
| 11-15 15:01 | +15 | ZEC | UP | 0.41 | 0.65 | 2.07 |
| 11-15 15:01 | +10 | ZEC | UP | 0.41 | 0.55 | 1.05 |
