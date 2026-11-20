# Range-Scalp Bot

*Updated Fri Nov 20 01:04 UTC. Paper money. Kalshi's 15-minute crypto up/down markets: when either side's price holds between 55¢ and 70¢ for 20 seconds, buy 10 contracts, sell at +5/+10/+15/+20¢, plus a +10¢ version that also cuts losses at −15¢ (five versions side by side), then look for the next one. Anything not sold rides to the close.*

[← Back to all bots](README.md)

## Verdict

🔴 **Losing overall.** The quick wins aren't covering the trades that never get there.

| Sell at | Trades | Sold early | Held to close (won) | Open | P&L | Return |
|---|---|---|---|---|---|---|
| **+5¢** | 65570 | 57237 | 8333 (124) | 8 | $-17553.62 | -4.3% |
| **+10¢** | 48974 | 39232 | 9742 (165) | 8 | $-16307.32 | -5.3% |
| **+15¢** | 41071 | 30562 | 10509 (211) | 9 | $-14674.37 | -5.7% |
| **+20¢** | 36567 | 25526 | 11041 (266) | 9 | $-12993.58 | -5.7% |
| **+10¢ (15¢ stop)** | 79827 | 79663 | 164 (98) | 5 | $-29369.77 | -5.9% |

## Latest trades

| Time (UTC) | Version | Coin | Side | Paid | Sold / result | P&L |
|---|---|---|---|---|---|---|
| 11-20 01:04 | +10 stop | BTC | DOWN | 0.53 | open |  |
| 11-20 01:04 | +10 stop | NEAR | DOWN | 0.69 | open |  |
| 11-20 01:04 | +20 | NEAR | DOWN | 0.69 | open |  |
| 11-20 01:04 | +15 | NEAR | DOWN | 0.69 | open |  |
| 11-20 01:04 | +10 | NEAR | DOWN | 0.70 | open |  |
| 11-20 01:04 | +5 | NEAR | DOWN | 0.70 | open |  |
| 11-20 01:03 | +10 stop | SOL | DOWN | 0.61 | open |  |
| 11-20 01:03 | +10 stop | DOGE | DOWN | 0.60 | open |  |
| 11-20 01:03 | +5 | BNB | DOWN | 0.59 | open |  |
| 11-20 01:03 | +10 stop | XRP | UP | 0.50 | 0.62 | 0.85 |
| 11-20 01:03 | +15 | XRP | UP | 0.50 | open |  |
| 11-20 01:03 | +10 | XRP | UP | 0.51 | 0.62 | 0.75 |
| 11-20 01:03 | +5 | XRP | UP | 0.51 | 0.62 | 0.75 |
| 11-20 01:03 | +20 | ZEC | UP | 0.61 | open |  |
| 11-20 01:02 | +10 stop | BNB | UP | 0.48 | open |  |
| 11-20 01:02 | +10 stop | BTC | UP | 0.62 | 0.45 | -2.05 |
| 11-20 01:02 | +10 stop | SOL | UP | 0.60 | 0.38 | -2.54 |
| 11-20 01:02 | +10 stop | ETH | UP | 0.65 | 0.49 | -1.94 |
| 11-20 01:02 | +10 stop | DOGE | UP | 0.70 | 0.45 | -2.83 |
| 11-20 01:02 | +10 stop | HYPE | UP | 0.68 | 0.49 | -2.24 |
| 11-20 01:02 | +15 | ZEC | UP | 0.71 | open |  |
| 11-20 01:02 | +10 stop | ZEC | UP | 0.69 | 0.52 | -2.03 |
| 11-20 01:02 | +10 | ZEC | UP | 0.69 | open |  |
| 11-20 01:02 | +5 | ZEC | UP | 0.69 | open |  |
| 11-20 01:02 | +10 stop | XRP | UP | 0.57 | 0.69 | 0.87 |
| 11-20 01:02 | +20 | XRP | UP | 0.57 | open |  |
| 11-20 01:02 | +15 | XRP | UP | 0.57 | 0.76 | 1.59 |
| 11-20 01:02 | +10 | XRP | UP | 0.57 | 0.69 | 0.87 |
| 11-20 01:02 | +5 | XRP | UP | 0.57 | 0.69 | 0.87 |
| 11-20 01:01 | +5 | NEAR | UP | 0.66 | 0.72 | 0.29 |
| 11-20 01:01 | +5 | BNB | DOWN | 0.52 | 0.60 | 0.45 |
| 11-20 01:01 | +10 stop | ETH | DOWN | 0.62 | 0.45 | -2.05 |
| 11-20 01:01 | +20 | ETH | DOWN | 0.62 | open |  |
| 11-20 01:01 | +15 | ETH | DOWN | 0.62 | open |  |
| 11-20 01:01 | +10 | ETH | DOWN | 0.61 | open |  |
| 11-20 01:01 | +5 | ETH | DOWN | 0.62 | open |  |
| 11-20 01:01 | +10 stop | DOGE | DOWN | 0.58 | 0.35 | -2.63 |
| 11-20 01:01 | +20 | DOGE | DOWN | 0.58 | open |  |
| 11-20 01:01 | +15 | DOGE | DOWN | 0.58 | open |  |
| 11-20 01:01 | +10 | DOGE | DOWN | 0.58 | open |  |
